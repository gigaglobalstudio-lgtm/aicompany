"""
Google Slides API Integration
Usage: python slides_api.py [action] [args]
Actions: create, add_slide, list
"""

import os
import sys
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Credentials path
CREDS_FILE = os.path.expanduser("~/.claude/google_credentials.json")
TOKEN_FILE = os.path.expanduser("~/.claude/google_token.json")

def get_credentials():
    """Load or refresh credentials."""
    creds = None

    # Try to load existing token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            token_data = json.load(f)
            creds = Credentials(
                token=token_data.get('access_token'),
                refresh_token=token_data.get('refresh_token'),
                token_uri='https://oauth2.googleapis.com/token',
                client_id=token_data.get('client_id'),
                client_secret=token_data.get('client_secret')
            )

    # Load from credentials file
    if not creds and os.path.exists(CREDS_FILE):
        with open(CREDS_FILE, 'r') as f:
            cred_data = json.load(f)
            installed = cred_data.get('installed', cred_data)
            creds = Credentials(
                token=None,
                refresh_token=installed.get('refresh_token'),
                token_uri='https://oauth2.googleapis.com/token',
                client_id=installed.get('client_id'),
                client_secret=installed.get('client_secret')
            )

    if creds and creds.expired and creds.refresh_token:
        from google.auth.transport.requests import Request
        creds.refresh(Request())
        # Save refreshed token
        save_token(creds)

    return creds

def save_token(creds):
    """Save token for future use."""
    token_data = {
        'access_token': creds.token,
        'refresh_token': creds.refresh_token,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret
    }
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_data, f)

def create_presentation(title):
    """Create a new presentation."""
    creds = get_credentials()
    service = build('slides', 'v1', credentials=creds)

    presentation = service.presentations().create(body={
        'title': title
    }).execute()

    print(f"Created presentation: {presentation.get('title')}")
    print(f"ID: {presentation.get('presentationId')}")
    print(f"URL: https://docs.google.com/presentation/d/{presentation.get('presentationId')}")

    return presentation

def add_slide(presentation_id, title, body_text):
    """Add a slide to existing presentation."""
    creds = get_credentials()
    service = build('slides', 'v1', credentials=creds)

    # Create new slide
    requests = [{
        'createSlide': {
            'slideLayoutReference': {
                'predefinedLayout': 'TITLE_AND_BODY'
            }
        }
    }]

    response = service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()

    slide_id = response.get('replies')[0].get('createSlide').get('objectId')

    # Get slide elements
    presentation = service.presentations().get(presentationId=presentation_id).execute()
    slide = None
    for s in presentation.get('slides', []):
        if s.get('objectId') == slide_id:
            slide = s
            break

    if slide:
        # Find title and body placeholders
        title_id = None
        body_id = None
        for element in slide.get('pageElements', []):
            shape = element.get('shape', {})
            placeholder = shape.get('placeholder', {})
            if placeholder.get('type') == 'TITLE':
                title_id = element.get('objectId')
            elif placeholder.get('type') == 'BODY':
                body_id = element.get('objectId')

        # Add text
        text_requests = []
        if title_id and title:
            text_requests.append({
                'insertText': {
                    'objectId': title_id,
                    'text': title
                }
            })
        if body_id and body_text:
            text_requests.append({
                'insertText': {
                    'objectId': body_id,
                    'text': body_text
                }
            })

        if text_requests:
            service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': text_requests}
            ).execute()

    print(f"Added slide: {title}")
    return slide_id

def list_presentations():
    """List recent presentations from Drive."""
    creds = get_credentials()
    drive_service = build('drive', 'v3', credentials=creds)

    results = drive_service.files().list(
        q="mimeType='application/vnd.google-apps.presentation'",
        pageSize=10,
        fields="files(id, name, createdTime)"
    ).execute()

    files = results.get('files', [])
    if not files:
        print("No presentations found.")
    else:
        print("Recent Presentations:")
        for f in files:
            print(f"  - {f['name']}")
            print(f"    ID: {f['id']}")
            print(f"    URL: https://docs.google.com/presentation/d/{f['id']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python slides_api.py create 'Presentation Title'")
        print("  python slides_api.py add_slide PRESENTATION_ID 'Slide Title' 'Body text'")
        print("  python slides_api.py list")
        sys.exit(1)

    action = sys.argv[1]

    if action == "create":
        title = sys.argv[2] if len(sys.argv) > 2 else "New Presentation"
        create_presentation(title)

    elif action == "add_slide":
        if len(sys.argv) < 4:
            print("Usage: python slides_api.py add_slide PRESENTATION_ID 'Title' 'Body'")
            sys.exit(1)
        pres_id = sys.argv[2]
        slide_title = sys.argv[3]
        slide_body = sys.argv[4] if len(sys.argv) > 4 else ""
        add_slide(pres_id, slide_title, slide_body)

    elif action == "list":
        list_presentations()

    else:
        print(f"Unknown action: {action}")
