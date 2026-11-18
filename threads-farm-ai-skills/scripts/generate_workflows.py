#!/usr/bin/env python3
"""Create importable n8n workflow scaffolds (not configured integrations)."""
import argparse, json, uuid
from pathlib import Path

N = "n8n-nodes-base."

def node(name, typ, x, y, parameters, type_version=1):
    return {"id": str(uuid.uuid5(uuid.NAMESPACE_URL, name)), "name": name,
            "type": N + typ, "typeVersion": type_version,
            "position": [x, y], "parameters": parameters}

def build(key, cfg):
    specs = {
        "draft": ("P1 - AI Drafts and Human Approval Queue", "draft_cron", "/v1/drafts/generate", "Soạn draft + lưu chờ duyệt", "Báo cáo tạo bản nháp", "drafts_created", "pending_review"),
        "publish": ("P3 - Approved Posts via Android Farm", "publish_cron", "/v1/posts/publish-approved", "Đăng bài đã duyệt qua Farm", "Báo cáo đăng bài", "published", "failed"),
        "metrics": ("P4 - Apify Daily Metrics Collection", "metrics_cron", "/v1/metrics/collect", "Thu thập số liệu bài đăng", "Báo cáo số liệu", "successful", "failed")}
    title, cron_key, endpoint, step, summary, ok_field, other_field = specs[key]
    trigger_name = 'Lập lịch tự động'
    webhook_name = 'Webhook kích hoạt'
    http_name = step
    report_name = summary
    url = cfg['adapter_base_url'].rstrip('/') + endpoint
    cron = cfg[cron_key]
    webhook_path = cfg['webhook_paths'][key]
    # n8n cron expression in interval; import and verify against target n8n version.
    trig = node(trigger_name, 'scheduleTrigger', 200, 190,
                {"rule":{"interval":[{"field":"cronExpression","expression":cron}]}},1.2)
    hook = node(webhook_name, 'webhook', 200, 390,
                {"httpMethod":"POST","path":webhook_path,"responseMode":"onReceived","options":{}},2)
    # Body built using an n8n expression; values are centrally authored here.
    payload = {"source":"n8n", "phase":key,"run_at":"={{ $now.toISO() }}",
               "batch_size":cfg['batch_size'],"accounts_count":cfg['accounts_count'],
               "posts_per_account_per_day":cfg['posts_per_account_per_day'],
               "enforce_approval":True,"only_published":True}
    # Use explicit JSON body expression to evaluate time safely.
    body_expr = '={{ JSON.stringify({"source":"n8n","phase":"' + key + '","run_at":$now.toISO(),"batch_size":' + str(cfg['batch_size']) + ',"accounts_count":' + str(cfg['accounts_count']) + ',"posts_per_account_per_day":' + str(cfg['posts_per_account_per_day']) + ',"enforce_approval":true,"only_published":true}) }}'
    http = node(http_name, 'httpRequest', 530, 290,
                {"method":"POST","url":url,"sendBody":True,"specifyBody":"json","jsonBody":body_expr,
                 "options":{"timeout":120000}},4.2)
    # Notifications are intentionally a manual setup step, to avoid fake operational Telegram.
    code = f"""const p = $input.first().json || {{}};
const ok = Number(p.{ok_field} ?? 0);
const other = Number(p.{other_field} ?? 0);
const message = `[Threads Farm / {key.upper()}] run=${{p.run_id ?? 'unknown'}}; {ok_field}=${{ok}}; {other_field}=${{other}}; sheet=${{p.sheet_url ?? p.review_sheet_url ?? '(not configured)'}}`;
return [{{json: {{phase: '{key}', message, run_id: p.run_id ?? null, status: 'REPORT_READY', telegram_setup_required: true, source_response: p}}}}];"""
    formatter = node(report_name, 'code', 850, 290, {"mode":"runOnceForAllItems","jsCode":code},2)
    notes = node('Cấu hình Telegram trước activation', 'stickyNote', 810, 70,
                 {"content":"⚠️ DRAFT SCAFFOLD. Configure Telegram bot/chat via Credentials and add a Telegram Send Message node after Report. Authenticate HTTP gateway/webhook, verify approval + idempotency, test before activation.","height":140,"width":450},1)
    nodes=[trig,hook,http,formatter,notes]
    return {"name":title, "nodes":nodes,
            "connections":{trigger_name:{"main":[[{"node":http_name,"type":"main","index":0}]]},
                           webhook_name:{"main":[[{"node":http_name,"type":"main","index":0}]]},
                           http_name:{"main":[[{"node":report_name,"type":"main","index":0}]]}},
            "settings":{"executionOrder":"v1","timezone":cfg['timezone']},
            "active":False,"pinData":{},"tags":[],
            "meta":{"templateCredsSetupCompleted":False,"threadsFarmPhase":key}}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--config',default='examples/project-config.json')
    ap.add_argument('--out',default='generated')
    args=ap.parse_args();cfg=json.loads(Path(args.config).read_text(encoding='utf-8'))
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    for key in ['draft','publish','metrics']:
        p=out/f'{key}-workflow.json'
        p.write_text(json.dumps(build(key,cfg),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'generated {p}')
if __name__=='__main__':main()
