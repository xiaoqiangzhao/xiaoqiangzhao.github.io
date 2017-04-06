#! /home/b51816/local/bin/python3
from SubmitJobs import SubmitJobs
from PlanAnalysis import XlsxParser
import sys
xlsx_file = sys.argv[1]
test = XlsxParser(xlsx_file)
test.parser()

re = SubmitJobs(test.json_file)
re.generate_compile_sh()
for v in re.vectors:
    if not v == 'null' :
        re.generate_simulate_sh(v)
re.gen_results()
