import unittest
from python_repos import summarize_github_repos


class SummarizeGithubReposTestCase(unittest.TestCase):
    """Tests for summarize_github_repos()."""

    def test_status_code(self):
        """Is the status code 200?"""
        summary = summarize_github_repos('python')
        self.assertEqual(summary, 200)


if __name__ == '__main__':
    unittest.main()