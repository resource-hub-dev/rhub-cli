from enum import Enum


class RhubApiLabClusterListClustersFilterStatus(str, Enum):
    ACTIVE = "Active"
    CREATE_FAILED = "Create Failed"
    DELETED = "Deleted"
    DELETE_FAILED = "Delete Failed"
    DELETING = "Deleting"
    DELETION_FAILED = "Deletion Failed"
    DELETION_QUEUED = "Deletion Queued"
    INSTALLATION_FAILED = "Installation Failed"
    INSTALLATION_QUEUED = "Installation Queued"
    INSTALLING = "Installing"
    POST_DELETING = "Post-Deleting"
    POST_DELETION_FAILED = "Post-Deletion Failed"
    POST_DELETION_QUEUED = "Post-Deletion Queued"
    POST_INSTALLATION_FAILED = "Post-Installation Failed"
    POST_INSTALLATION_QUEUED = "Post-Installation Queued"
    POST_INSTALLING = "Post-Installing"
    POST_PROVISIONING = "Post-Provisioning"
    POST_PROVISIONING_FAILED = "Post-Provisioning Failed"
    POST_PROVISIONING_QUEUED = "Post-Provisioning Queued"
    PRE_DELETING = "Pre-Deleting"
    PRE_DELETION_FAILED = "Pre-Deletion Failed"
    PRE_DELETION_QUEUED = "Pre-Deletion Queued"
    PRE_INSTALLATION_FAILED = "Pre-Installation Failed"
    PRE_INSTALLATION_QUEUED = "Pre-Installation Queued"
    PRE_INSTALLING = "Pre-Installing"
    PRE_PROVISIONING = "Pre-Provisioning"
    PRE_PROVISIONING_FAILED = "Pre-Provisioning Failed"
    PRE_PROVISIONING_QUEUED = "Pre-Provisioning Queued"
    PROVISIONING = "Provisioning"
    PROVISIONING_FAILED = "Provisioning Failed"
    PROVISIONING_QUEUED = "Provisioning Queued"
    QUEUED = "Queued"

    def __str__(self) -> str:
        return str(self.value)
