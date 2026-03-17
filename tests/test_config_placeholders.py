import unittest

from config import is_placeholder_env_value


class PlaceholderConfigTests(unittest.TestCase):
    def test_detects_example_placeholders(self) -> None:
        self.assertTrue(is_placeholder_env_value("EMAIL_API_URL", "https://your-mail-api.example.com"))
        self.assertTrue(is_placeholder_env_value("EMAIL_API_TOKEN", "replace-with-your-token"))
        self.assertTrue(is_placeholder_env_value("EMAIL_DOMAIN", "example.com"))
        self.assertTrue(is_placeholder_env_value("EMAIL_DOMAINS", "example.org"))
        self.assertTrue(is_placeholder_env_value("SERVER_URL", "https://your-server.example.com"))
        self.assertTrue(is_placeholder_env_value("SERVER_ADMIN_PASSWORD", "replace-with-your-admin-password"))

    def test_allows_real_values(self) -> None:
        self.assertFalse(is_placeholder_env_value("EMAIL_API_URL", "https://mail.nashome.me"))
        self.assertFalse(is_placeholder_env_value("EMAIL_API_TOKEN", "abc123-real-token"))
        self.assertFalse(is_placeholder_env_value("EMAIL_DOMAIN", "nashome.me"))
        self.assertFalse(is_placeholder_env_value("SERVER_URL", "https://search.hunters.works"))
        self.assertFalse(is_placeholder_env_value("SERVER_ADMIN_PASSWORD", "Jelly120425"))


if __name__ == "__main__":
    unittest.main()
