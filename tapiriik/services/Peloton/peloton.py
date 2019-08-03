from tapiriik.services.service_base import ServiceAuthenticationType, ServiceBase
from tapiriik.services.interchange import ActivityType

import logging

logger = logging.getLogger(__name__)

class PelotonService(ServiceBase):
    ID = "peloton"
    DisplayName = "Peloton"
    DisplayAbbreviation = "PL"
    AuthenticationType = ServiceAuthenticationType.UsernamePassword
    RequiresExtendedAuthorizationDetails = True
    PartialSyncRequiresTrigger = True

    SupportsActivityDeletion = False

    SupportsHR = SupportsCadence = SupportsPower = SupportsCalories = True

    # For mapping common->Peloton; no ambiguity in Peloton activity type
    _activityTypeMappings = {
        ActivityType.Cycling: "Ride",
        ActivityType.Running: "Run",
        ActivityType.Walking: "Walk",
    }

    # For mapping Peloton->common
    _reverseActivityTypeMappings = {
        "Ride": ActivityType.Cycling,
        "Run": ActivityType.Running,
        "Walk": ActivityType.Walking,
    }

    SupportedActivities = list(_activityTypeMappings.keys())
