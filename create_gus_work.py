#!/usr/bin/env python3
"""
GUS Work Item Creator - Creates Salesforce GUS work items with minimal input.
Requires: pip install simple-salesforce python-dotenv
"""

import os
import sys
from datetime import datetime
from simple_salesforce import Salesforce
from dotenv import load_dotenv

load_dotenv()

# Sensible defaults
DEFAULTS = {
    'RecordTypeId': os.getenv('GUS_RECORDTYPE_ID', '012B00000008xSvIAI'),  # User Story
    'Priority__c': 'P2 - Medium',
    'Status__c': 'New',
    'Assignee__c': os.getenv('GUS_DEFAULT_ASSIGNEE'),
    'Product_Tag__c': os.getenv('GUS_DEFAULT_PRODUCT_TAG'),
    'Team__c': os.getenv('GUS_DEFAULT_TEAM'),
    'Sprint__c': os.getenv('GUS_DEFAULT_SPRINT'),
}

def get_salesforce_client():
    """Initialize Salesforce connection."""
    username = os.getenv('SF_USERNAME')
    password = os.getenv('SF_PASSWORD')
    security_token = os.getenv('SF_SECURITY_TOKEN')
    domain = os.getenv('SF_DOMAIN', 'login')

    if not all([username, password, security_token]):
        print("Error: Missing Salesforce credentials in .env file")
        print("Required: SF_USERNAME, SF_PASSWORD, SF_SECURITY_TOKEN")
        sys.exit(1)

    return Salesforce(
        username=username,
        password=password,
        security_token=security_token,
        domain=domain
    )

def create_work_item(sf, subject, description=None, work_type='Story', priority=None):
    """Create a GUS work item with minimal required fields."""

    work_item = {
        'Subject': subject,
        'RecordTypeId': DEFAULTS['RecordTypeId'],
        'Priority__c': priority or DEFAULTS['Priority__c'],
        'Status__c': DEFAULTS['Status__c'],
    }

    if description:
        work_item['Description__c'] = description

    # Add defaults if configured
    if DEFAULTS.get('Assignee__c'):
        work_item['Assignee__c'] = DEFAULTS['Assignee__c']
    if DEFAULTS.get('Product_Tag__c'):
        work_item['Product_Tag__c'] = DEFAULTS['Product_Tag__c']
    if DEFAULTS.get('Team__c'):
        work_item['Team__c'] = DEFAULTS['Team__c']
    if DEFAULTS.get('Sprint__c'):
        work_item['Sprint__c'] = DEFAULTS['Sprint__c']

    try:
        result = sf.ADM_Work__c.create(work_item)
        return result
    except Exception as e:
        print(f"Error creating work item: {e}")
        sys.exit(1)

def main():
    """Main function - minimal questions, smart defaults."""

    # Quick create mode: python create_gus_work.py "Title" "Description"
    if len(sys.argv) >= 2:
        subject = sys.argv[1]
        description = sys.argv[2] if len(sys.argv) >= 3 else None
        priority = sys.argv[3] if len(sys.argv) >= 4 else None
    else:
        # Interactive mode - still minimal
        subject = input("Title: ").strip()
        if not subject:
            print("Error: Title is required")
            sys.exit(1)

        description = input("Description (optional, press Enter to skip): ").strip() or None
        priority = input("Priority (optional, press Enter for P2): ").strip() or None

    print("\nCreating work item...")
    sf = get_salesforce_client()
    result = create_work_item(sf, subject, description, priority=priority)

    if result['success']:
        work_id = result['id']
        gus_url = f"https://gus.lightning.force.com/lightning/r/ADM_Work__c/{work_id}/view"
        print(f"\n✓ Work item created successfully!")
        print(f"  ID: {work_id}")
        print(f"  URL: {gus_url}")
    else:
        print(f"\n✗ Failed to create work item")
        sys.exit(1)

if __name__ == "__main__":
    main()
