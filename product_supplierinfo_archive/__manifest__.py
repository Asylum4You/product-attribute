# Copyright 2021 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

{
    "name": "Product Supplier Info Archive",
    "summary": """
        Add the active field to the product supplier info
        """,
    "version": "14.0.1.1.0",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/product-attribute",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "depends": ["product"],
    "data": ["data/ir_cron.xml", "views/product_views.xml"],
    "installable": True,
    "maintainers": ["GuillemCForgeFlow", "AlvaroTForgeFlow", "OriolVForgeFlow"],
}
