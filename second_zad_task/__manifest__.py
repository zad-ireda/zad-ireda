# -*- coding: utf-8 -*-

{
    'name': "second_zad ",
    'version' : '1.2',
    'sequence':-100,
    'depends':['base','auth_signup'],
    'data':['security/ir.model.access.csv',
            'views/res_user_inherit.xml',
            'views/sign_up_templete.xml'],
            
    'application':True,   
}


# {
#     'name': 'CRM',
#     'version': '1.2',
#     'category': 'Sales/CRM',
#     'sequence': 15,
#     'summary': 'Track leads and close opportunities',
#     'description': "",
#     'website': 'https://www.odoo.com/page/crm',
#     'depends': [
#         'base_setup',
#         'sales_team',
#         'mail',
#         'calendar',
#         'resource',
#         'fetchmail',
#         'utm',
#         'web_tour',
#         'contacts',
#         'digest',
#         'phone_validation',
#     ],
#     'data': [
#         'security/crm_security.xml',
#         'security/ir.model.access.csv',

#         'data/crm_lead_prediction_data.xml',
#         'data/crm_lost_reason_data.xml',
#         'data/crm_stage_data.xml',
#         'data/crm_team_data.xml',
#         'data/digest_data.xml',
#         'data/mail_data.xml',
#         'data/crm_recurring_plan_data.xml',

#         'wizard/crm_lead_lost_views.xml',
#         'wizard/crm_lead_to_opportunity_views.xml',
#         'wizard/crm_lead_to_opportunity_mass_views.xml',
#         'wizard/crm_merge_opportunities_views.xml',

#         'views/assets.xml',
#         'views/calendar_views.xml',
#         'views/crm_recurring_plan_views.xml',
#         'views/crm_menu_views.xml',
#         'views/crm_lost_reason_views.xml',
#         'views/crm_stage_views.xml',
#         'views/crm_lead_views.xml',
#         'views/digest_views.xml',
#         'views/mail_activity_views.xml',
#         'views/res_config_settings_views.xml',
#         'views/res_partner_views.xml',
#         'views/utm_campaign_views.xml',
#         'report/crm_activity_report_views.xml',
#         'report/crm_opportunity_report_views.xml',
#         'views/crm_team_views.xml',
#     ],
#     'demo': [
#         'data/crm_team_demo.xml',
#         'data/mail_activity_demo.xml',
#         'data/crm_lead_demo.xml',
#     ],
#     'css': ['static/src/css/crm.css'],
#     'installable': True,
#     'application': True,
#     'auto_install': False
# }