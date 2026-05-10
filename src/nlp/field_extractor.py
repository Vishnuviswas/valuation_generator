import re

# -------------------------------------------------
# BASIC CLEANER
# -------------------------------------------------
def clean_text(value):
    if value is None:
        return ""

    if not isinstance(value, str):
        return value

    value = value.replace("\n", " ")
    value = value.strip()
    value = value.lstrip(":|.-, ")
    value = value.rstrip("|. ")
    value = " ".join(value.split())

    return value


# -------------------------------------------------
# GLOBAL LOCATION EXTRACTOR (KEY FIX)
# -------------------------------------------------
def extract_location_global(text, keyword):
    pattern = rf"\b([A-Za-z ]{{2,50}}?)\s+{keyword}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)

    if not matches:
        return ""

    value = matches[-1]
    value = re.sub(r"^(of|in)\s+", "", value, flags=re.IGNORECASE)

    return clean_text(value)


# -------------------------------------------------
# EXTENT (ARES)
# -------------------------------------------------
def extract_extent_ares(text):
    match = re.search(r"([\d\.]+)\s*ares", text, re.IGNORECASE)
    return match.group(1) if match else ""


# -------------------------------------------------
# SIMPLE KEY-VALUE FIELDS
# -------------------------------------------------
def extract_field(text, keywords):
    for key in keywords:
        pattern = rf"{key}\s*[:\-]\s*([A-Za-z0-9 ,./()-]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return clean_text(match.group(1))
    return ""


# -------------------------------------------------
# ✅ FIXED BOUNDARIES (MULTILINE SAFE)
# -------------------------------------------------
def extract_boundary(text, direction):
    if not text:
        return ""

    # Normalize tabs
    text = text.replace("\t", " ")

    # Match:
    # East   : PWD Road
    # East: PWD Road
    # East - PWD Road
    pattern = rf"{direction}\s*[\n\r]*\s*[:\-]\s*(.+)"

    matches = re.findall(pattern, text, re.IGNORECASE)

    if not matches:
        return ""

    # Take first valid match and stop at end of line
    value = matches[0].split("\n")[0]

    return clean_text(value)


# -------------------------------------------------
# MAIN EXTRACTOR (PRODUCTION READY)
# -------------------------------------------------
def extract_all_fields(text):
    fields = {}

    fields["borrower"] = extract_field(
        text,
        ["Borrower", "Name of the Borrower", "owned by","Name of the Owner","Applicant"]
    )

    fields["survey_no"] = extract_field(
        text,
        ["Re Survey No", "Resurvey No", "Survey No","Re-Sy No","Sy No"]
    )

    fields["village"] = extract_location_global(text, "Village") or extract_field(text, ["Village"])
    fields["taluk"] = extract_location_global(text, "Taluk") or extract_field(text, ["Taluk"])
    fields["district"] = extract_location_global(text, "District")

    fields["extent_ares"] = extract_extent_ares(text)

    fields["boundary_east"] = extract_boundary(text, "East")
    fields["boundary_west"] = extract_boundary(text, "West")
    fields["boundary_north"] = extract_boundary(text, "North")
    fields["boundary_south"] = extract_boundary(text, "South")

    return fields
