from odoo import fields, models

class HrEmployeePublicInherit(models.Model):
    _inherit = 'hr.employee.public'

    branch_id = fields.Many2one('employee.branch', string='Branch', related='employee_id.branch_id', readonly=False)
    agent_number = fields.Char('Voxbay Agent Number', readonly=False)
    related_joinee = fields.Many2one('employee.joining.form', string='Related Joinee', related='employee_id.related_joinee', readonly=False)
    biometric_no = fields.Char(string='Biometric Code', related='employee_id.biometric_no', readonly=False)
    # voxbay_agent_number_outgoing = fields.Char(string="Voxbay Agent Number Outgoing", readonly=False)
    
    blood_group = fields.Char(string='Blood Group')
    emergency_contact_person_relationship = fields.Char(string='Emergency Contact Person Relationship')
    emergency_contact_person_email = fields.Char(string='Emergency Contact Person Email')
    emergency_contact_person_correspondence_address = fields.Char(
        string='Emergency Contact Person Correspondence Address')

    bank_name = fields.Char(string='Bank Name')
    branch_bank = fields.Char(string='Branch')
    ifsc_code = fields.Char(string='IFSC Code')

    spouse_name = fields.Char(string='Spouse Name')

    date_of_joining = fields.Date(string='Date Of Joining')

    previous_employment_company_name = fields.Char(string='Previous Employment - Company Name')
    previous_employment_company_location = fields.Char(string='Previous Employment - Company Location')
    previous_employment_company_designation = fields.Char(string='Previous Employment - Company Designation')
    total_years_of_experience = fields.Integer(
        string='Total Years Of Experience')

    aadhar_card_number = fields.Char(string='Aadhar Card Number')
    pan_card_number = fields.Char(string='Pan Card Number')

    academic_department = fields.Boolean(related='department_id.is_academic', string="Academic Department", store=True)