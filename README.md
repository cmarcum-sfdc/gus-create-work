# GUS Work Item Creator

Create Salesforce GUS work items with minimal questions using sensible defaults.

## Quick Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure credentials:
```bash
cp .env.example .env
# Edit .env with your Salesforce credentials
```

3. Make script executable:
```bash
chmod +x create_gus_work.py
```

## Usage

### One-liner (fastest):
```bash
./create_gus_work.py "Fix login bug" "Users cannot login after password reset"
```

### With priority:
```bash
./create_gus_work.py "Critical bug" "Production is down" "P0"
```

### Interactive mode:
```bash
./create_gus_work.py
```

## Configuration

Set defaults in `.env` to avoid repeated questions:
- `GUS_DEFAULT_ASSIGNEE` - Auto-assign to you
- `GUS_DEFAULT_TEAM` - Your team
- `GUS_DEFAULT_PRODUCT_TAG` - Your product
- `GUS_DEFAULT_SPRINT` - Current sprint

## Getting Your Salesforce Security Token

1. Log into Salesforce
2. Go to Settings → Reset My Security Token
3. Check your email for the token
4. Add to `.env` file

## Finding IDs

To find user/team/sprint IDs:
```bash
# In Salesforce, go to the record and check the URL
# Example: /lightning/r/ADM_Sprint__c/a07xx000000ABCD/view
# The ID is: a07xx000000ABCD
```
