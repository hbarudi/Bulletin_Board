# Bulletin Board (Sticky Notes Application)

**Author:** Hashem Barudi  
**Course:** Django Web Development

---

## 📝 Note to Grader regarding Project Name
Per the instructions, the project was initially described as a "Bulletin Board" in the tutorial section, but the final task asked for "sticky_notes." I decided to stick with the name **`bulletin_board`** for the main project directory to maintain consistency with the initial setup steps I followed. The functionality remains identical to the Sticky Notes requirements.

---

## 📋 Project Description
This is a Django-based web application that allows users to manage "Sticky Notes." It implements the **MVT (Model-View-Template)** architecture and full **CRUD (Create, Read, Update, Delete)** functionality. It functions like a generic website that lets users put comments.

### Key Features
*   **Create Notes:** Add new notes with a title and content.
*   **View Notes:** See a list of all notes (Homepage) and view details of individual notes.
*   **Update Notes:** Edit existing notes.
*   **Delete Notes:** Remove notes (includes a "Are you sure?" confirmation).
*   **Custom Theme:** Implements a "Dark Orange" High-Contrast color scheme.

### 📂 Project Structure
*   **`bulletin_board_core/`**: Main Django configuration.
*   **`notes/`**: The main application handling the logic.
*   **`diagrams/`**: Contains the UML Use Case, Sequence, and Class diagrams.
*   **`research_answers.md`**: Answers to the research questions in Part 2.

---

## 🚀 How to Run the Project

1.  **Open the terminal** in the project root folder.

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Collect Static Files** (for CSS):
    ```bash
    python manage.py collectstatic
    ```

5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    *(Note: If port 8000 is blocked, try `python manage.py runserver 8080`)*

6.  **Open Browser:**
    Navigate to `http://127.0.0.1:8000/` (or your specific port).

---

## 🎨 Design & Diagrams
The design documents (Use Case, Sequence, and Class Diagrams) are located in the **`diagrams/`** folder within this project.