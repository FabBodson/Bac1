import unittest
from recrutement import match_skills


class MatchTest(unittest.TestCase):
    def setUp(self):
        self.candidate_skills = [
            {"name": "C#", "experience": 4, "preference": "neutral"},
            {"name": "JavaScript", "experience": 7, "preference": "neutral"},
            {"name": "Cpp", "experience": 4, "preference": "desired"},
            {"name": "Python", "experience": 1, "preference": "avoid"},
        ]

    def test_matches_found(self):
        job_skills = [
            {"name": "JavaScript", "idealYears": 6},
            {"name": "Cpp", "idealYears": 4}
        ]

        self.assertTrue(match_skills(self.candidate_skills, job_skills))

    def test_matches_found_trough_boost(self):
        job_skills = [
            {"name": "JavaScript", "idealYears": 6},
            {"name": "Cpp", "idealYears": 6}
        ]

        self.assertTrue(match_skills(self.candidate_skills, job_skills))

    def test_matches_not_found(self):
        job_skills = [
            {"name": "Rust", "idealYears": 0},
            {"name": "Swift", "idealYears": 7}
        ]

        self.assertFalse(match_skills(self.candidate_skills, job_skills))

    def test_matches_not_found_despite_boost(self):
        job_skills = [
            {"name": "JavaScript", "idealYears": 6},
            {"name": "Cpp", "idealYears": 7}
        ]

        self.assertFalse(match_skills(self.candidate_skills, job_skills))

    def test_matches_not_found_due_to_avoid(self):
        job_skills = [
            {"name": "Python", "idealYears": 0},
            {"name": "Cpp", "idealYears": 7}
        ]

        self.assertFalse(match_skills(self.candidate_skills, job_skills))


if __name__ == '__main__':
    unittest.main()
