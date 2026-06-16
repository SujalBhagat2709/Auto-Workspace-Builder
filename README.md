# Auto Workspace Builder

## Overview

Automatically generates a project workspace based on a project idea.

---

## Files

- workspace_analyzer.py
- workspace_builder.py

---

## Run

```bash
python workspace_builder.py
```

---

## Example

Input:

```text
auction platform
```

Output:

```text
auction-platform/

backend/
frontend/
database/

users/
auctions/
bids/
payments/

README.md
```

---

Input:

```text
hospital management system
```

Output:

```text
hospital-management/

backend/
frontend/
database/

patients/
doctors/
appointments/
billing/

README.md
```

---

## Future Improvements

- AI Module Detection
- React Templates
- FastAPI Templates
- Database Schema Generation
- API Generation
- Docker Support