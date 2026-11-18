import json, unittest, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from generate_workflows import build
from validate_workflows import validate

class WorkflowGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.cfg=json.loads((ROOT/'examples/project-config.json').read_text())
    def test_generation_each_phase(self):
        for phase in ('draft','publish','metrics'):
            w=build(phase,self.cfg)
            self.assertFalse(w['active'])
            self.assertEqual(len([x for x in w['nodes'] if x['type'].endswith('webhook')]),1)
            self.assertEqual(len([x for x in w['nodes'] if x['type'].endswith('scheduleTrigger')]),1)
            self.assertTrue(any('/v1/' in n.get('parameters',{}).get('url','') for n in w['nodes']))
    def test_approval_guard_requested(self):
        w=build('publish',self.cfg)
        http=next(n for n in w['nodes'] if n['type'].endswith('httpRequest'))
        self.assertIn('enforce_approval',http['parameters']['jsonBody'])
    def test_files_validate(self):
        for file in (ROOT/'generated').glob('*.json'):
            self.assertEqual(validate(file),[],file.name)
if __name__=='__main__': unittest.main()
