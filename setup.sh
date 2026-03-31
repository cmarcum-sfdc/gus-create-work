#!/bin/bash
# Quick setup script

echo "🚀 Setting up GUS Work Item Creator..."

# Install dependencies
pip install -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file - please edit with your credentials"
else
    echo "✓ .env file already exists"
fi

# Make script executable
chmod +x create_gus_work.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your Salesforce credentials"
echo "2. Run: ./create_gus_work.py \"Your work item title\""
echo ""
echo "Optional: Add alias to your ~/.zshrc:"
echo "  alias gus='~/Desktop/onsite/gus-create-work/create_gus_work.py'"
