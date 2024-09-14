import time
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CustomSales(models.Model):
    _inherit = "account.move"
    
    test_field = fields.Char(string="Text")
