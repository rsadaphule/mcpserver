from mcp.server.fastmcp import FastMCP
import os

# create an MCP Server
mcp = FastMCP("AI Notes Server")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

def log(message: str):
    print(message)

@mcp.tool()
def add_note(note: str) -> str:
    """
    Add a new note to the notes file.
    
    This function appends a note to the persistent notes file. The note is added
    as-is without any formatting, timestamps, or separators. If the notes file
    doesn't exist, it will be created automatically.
    
    Args:
        note (str): The note content to be added to the file. Can contain any
                   text including newlines, special characters, and unicode.
                   Empty strings are allowed but will result in no visible
                   content being added.
    
    Returns:
        str: Always returns "Note added successfully" upon successful completion.
             This is a confirmation message indicating the operation completed
             without errors.
    
    Side Effects:
        - Creates the notes file (notes.txt) if it doesn't exist
        - Appends the note content to the existing notes file
        - No automatic formatting, timestamps, or separators are added
    
    Examples:
        >>> add_note("Remember to buy groceries")
        'Note added successfully'
        
        >>> add_note("Meeting with team at 3 PM\\nDiscuss project timeline")
        'Note added successfully'
        
        >>> add_note("")  # Empty note
        'Note added successfully'
    
    Note:
        - Notes are appended without any automatic newline characters
        - If you want notes on separate lines, include \\n at the end of each note
        - The function doesn't validate or sanitize input content
        - File operations may raise IOError if there are permission issues
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    return "Note added successfully"

@mcp.tool()
def get_notes() -> str:
    """
    Get all notes from the notes file.
    
    This function reads the notes file and returns all the notes as a string.
    If the notes file doesn't exist, it will be created automatically.
    
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read()
    return notes or "No notes found"








@mcp.resource("notes://latest")
def get_latestnote() -> str:
    """
    Get the latest note from the notes file.
    
    This function reads the notes file and returns the latest note as a string.
    If the notes file doesn't exist, it will be created automatically.
    
    """    
    ensure_file()
    int_note_id = -1
    notes=""
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
        log("from get_latest_notes: " + str(notes))
        log("first line" + str(notes[0]))
        log("last line" + str(notes[-1]))
        log("length of notes" + str(len(notes)))
    return notes[int_note_id].strip() 


@mcp.prompt()
def note_summary_prompt() -> str :
    """
    Summarize the notes file.
    
    This function reads the notes file and returns a summary of the notes.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read()
    if not notes:
        return  "No notes found"
    else:
        return f"summarize the notes in 2 or 3 sentences at most : {notes}"

def main():
    print("Hello from notes server!")


if __name__ == "__main__":
        main()
