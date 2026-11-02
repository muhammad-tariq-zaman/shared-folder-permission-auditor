import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import audit_row


def row(p, a):
    return {"share": "s", "path": "p", "principal": p, "access": a}


class TestShareAudit(unittest.TestCase):
    def test_everyone_full_is_high(self):
        self.assertEqual(audit_row(row("Everyone", "Full Control")), "HIGH")

    def test_everyone_change_is_medium(self):
        self.assertEqual(audit_row(row("Everyone", "Change")), "MEDIUM")

    def test_named_full_is_info(self):
        self.assertEqual(audit_row(row("IT Team", "Full Control")), "INFO")

    def test_read_is_ok(self):
        self.assertEqual(audit_row(row("Everyone", "Read")), "OK")
