def match_skills(candidate_skills, job_skills):
    for competence in job_skills:
        for compt_candidat in candidate_skills:

            if competence["name"] in compt_candidat["name"]:

                if compt_candidat["preference"] == "avoid":
                    print('avoid')
                    return False

                elif compt_candidat["preference"] == "desired":
                    #compt_candidat["experience"] += compt_candidat["experience"] / 2
                    compt_candidat["experience"] *= 1.5
                    print('boost')

                    if compt_candidat["experience"] >= competence["idealYears"]:
                        return True

                    else:
                        print('boost insuffisant')
                        return False

                else:

                    if compt_candidat["experience"] >= competence["idealYears"]:
                        print('ok')
                        return True
                    else:
                        return False
    print('oups')
    return False


def _main():
    candidat = [
        {"name": "C#", "experience": 4, "preference": "neutral"},
        {"name": "JavaScript", "experience": 7, "preference": "neutral"},
        {"name": "Cpp", "experience": 4, "preference": "desired"},
        {"name": "Python", "experience": 1, "preference": "avoid"},
    ]

    job = [
        {"name": "JavaScript", "idealYears": 6},
        {"name": "Cpp", "idealYears": 6}
    ]

    print(match_skills(candidat, job))


if __name__ == '__main__':
    _main()
