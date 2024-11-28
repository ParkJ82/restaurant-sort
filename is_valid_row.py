def is_valid_row(row, search_term, excluded_terms):
    """Check if a CSV row meets the required filtering conditions."""
    name, address = row.get("사업장명", ""), row.get("지번주소", "")
    return (
        search_term in address and
        row.get("영업상태명", "") != "폐업" and
        row.get("업태구분명", "") not in excluded_terms and
        not any(term in name for term in excluded_terms)
    )