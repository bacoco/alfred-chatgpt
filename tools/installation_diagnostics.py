"""Classify supplied repository observations; never change GitHub settings."""
from collections.abc import Mapping


def diagnose_repository(facts: Mapping) -> dict:
    """Unknown is distinct from False; callers must supply fresh authorized facts."""
    def result(state, actor, action):
        return {"state": state, "actor": actor, "next_action": action,
                "change_permissions": False, "activate_business": False}

    if facts.get("security_blocked") is True:
        return result("blocked", "owner", "resolve_explicit_block_without_bypass")
    if facts.get("conversation_refused") is True:
        return result("conversation_refused", "owner", "same_connector_chat_branch_then_read")
    if facts.get("accessible") is True and facts.get("exists") is False:
        return result("observations_conflict", "chat", "reread_metadata_before_any_action")
    if facts.get("owner_matches") is False:
        return result("wrong_owner", "owner", "confirm_correct_destination")
    if facts.get("private") is False:
        return result("public_repository", "owner", "make_private_then_reverify")
    if facts.get("exists") is False and facts.get("absence_verified") is True:
        if facts.get("owner_matches") is not True:
            return result("identity_unknown", "chat", "verify_identity_read_only")
        if facts.get("can_create_repository") is True:
            return result("repository_absent", "chat", "create_agreed_private_repository")
        return result("repository_absent", "owner", "create_private_repository_with_readme")
    if facts.get("accessible") is not True:
        if (facts.get("exists") is True and facts.get("private") is True and
                facts.get("github_app_excluded") is True):
            return result("private_not_selected", "owner", "review_installed_github_app_repository_access")
        return result("access_unknown", "chat", "report_exact_error_without_guessing_cause")
    if facts.get("private") is not True or facts.get("owner_matches") is not True:
        return result("identity_unknown", "chat", "verify_identity_and_private_visibility")
    if facts.get("can_write") is not True:
        return result("write_unavailable", "owner", "report_missing_write_capability")
    if facts.get("empty") is True:
        action = ("initialize_existing_private_repository" if facts.get("can_initialize") is True
                  else "add_initial_readme_then_reverify")
        return result("empty_private_repository", "chat" if facts.get("can_initialize") is True else "owner", action)
    if facts.get("scaffold") == "partial":
        return result("partial_scaffold", "chat", "reconcile_missing_files_without_overwrite")
    if facts.get("scaffold") == "complete":
        if facts.get("storage_readback_verified") is True:
            return result("storage_verified", "chat", "resume_or_request_only_missing_scope")
        return result("readback_required", "chat", "read_and_compare_all_required_files")
    return result("inventory_required", "chat", "inventory_existing_files_before_scaffold")
