#!/usr/bin/env python
import sys,os
from match_to_proposal.crew import MatchToProposalCrew
from src.match_to_proposal.tools.ResumeReader import convert_pdf_to_md

os.environ["OPENAI_API_KEY"]="API_KEY"
os.environ['OPENAI_MODEL_NAME']= "llama-3.1-70b-versatile"
os.environ['OPENAI_API_BASE']="https://api.groq.com/openai/v1"

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information

    # dicts_paths={f"path_to_cv_{i}":str(file) for i,file in enumerate(os.listdir('src\\match_to_proposal\\data\\CVs'))}
    # print(dicts_paths)
    # {'path_to_cv_0': 'Ashish_tandon.pdf', 'path_to_cv_1': 'Guru_sharan.pdf', 'path_to_cv_2': 'Vikas Resume (1).pdf', 'path_to_cv_3': 'VInayPvvsr (1).pdf', 'path_to_cv_4': 'Viviek_chabra.pdf'}
    inputs = {
        'path_to_jobs_md': 'src/match_to_proposal/data/jobs.md',
        'path_to_cv_0': 'src/match_to_proposal/data/CVs/Ashish_tandon.md',
        "path_to_cv_1":"src/match_to_proposal/data/CVs/Guru_sharan.md",
        "path_to_cv_2":"src/match_to_proposal/data/CVs/Vikas Resume (1).md",
        "path_to_cv_3":"src/match_to_proposal/data/CVs/VInayPvvsr (1).md",
        "path_to_cv_4":"src/match_to_proposal/data/CVs/Viviek_chabra.md"
        #'path_to_cv' : 'src\\match_to_proposal\\data\\CV'
        # dicts_paths[0]
    }
    for file in os.listdir("src\\match_to_proposal\\data\\CVs"):
        if file.endswith('.pdf'):
            convert_pdf_to_md(os.path.join("src\\match_to_proposal\\data\\CVs",file))
    MatchToProposalCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'path_to_jobs_csv': 'src/match_to_proposal/data/jobs.csv',
        #'path_to_cv' : 'src\\match_to_proposal\\data\\CV'
        'path_to_cv' :  'src/match_to_proposal/data/cv.md',
        'path_to_cv2':  'src/match_to_proposal/data/cv2.md',
        'path_to_cv3':  'src/match_to_proposal/data/cv3.md',
        'path_to_cv4':  'src/match_to_proposal/data/cv4.md',
        'path_to_cv5':  'src/match_to_proposal/data/cv5.md'

    }
    try:
        MatchToProposalCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
