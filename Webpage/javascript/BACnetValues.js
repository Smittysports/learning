
/** This table contains all of the BACnet Property IDs. The table is organized in the
 * following fashion:
 *
 * ID   PropertyName
 * --   ------------
 * 0    acked-transitions
 * 1    ack-required
 * ...
 * 
 * This is a template to use for a BACnet Property ID. This object can be created and
 * added to the BACnetPropertyIDs table:
 * 
 *   let BACnetPropertyID = {
 *       "ID": 0,
 *       "PropertyName": "acked-transitions"
 *   }
 */
let BACnetPropertyIDs = []

/** Helper method to add a new BACnetPropertyID to the BACnetPropertyIDs table
 */
function pushPropertyToTable(id, name, BACpypesName) {
    let BACnetPropertyID = {
        "ID": id,
        "BACnet Property ID Name": name,
        "BACpypes property ID name": BACpypesName
    }
    BACnetPropertyIDs.push(BACnetPropertyID)
}

/** Get the BACnet Property IDs from the server and display them in a table.
 *
 * TODO: The IDs are currently hard coded and placed into a table, these should be
 * retrieved from a server to make sure they are accurate and the data is created
 * in one place.
 */
function getPropertyIDs() {
    pushPropertyToTable(0, "acked-transitions","","")
    pushPropertyToTable(1, "ack-required","","")
    pushPropertyToTable(2, "action","action")
    pushPropertyToTable(3, "action-text","")
    pushPropertyToTable(4, "active-text","")
    pushPropertyToTable(5, "active-vt-sessions","")
    pushPropertyToTable(6, "alarm-value","")
    pushPropertyToTable(7, "alarm-values","")
    pushPropertyToTable(8, "all","all")
    pushPropertyToTable(9, "all-writes-successful","")
    pushPropertyToTable(10, "apdu-segment-timeout","")
    pushPropertyToTable(11, "apdu-timeout","")
    pushPropertyToTable(12, "application-software-version","")
    pushPropertyToTable(13, "archive","archive")
    pushPropertyToTable(14, "bias","bias")
    pushPropertyToTable(15, "change-of-state-count","")
    pushPropertyToTable(16, "change-of-state-time","")
    pushPropertyToTable(17, "notification-class","")
    pushPropertyToTable(19, "controlled-variable-reference","")
    pushPropertyToTable(20, "controlled-variable-units","")
    pushPropertyToTable(21, "controlled-variable-value","")
    pushPropertyToTable(22, "cov-increment","")
    pushPropertyToTable(23, "date-list","")
    pushPropertyToTable(24, "daylight-savings-status","")
    pushPropertyToTable(25, "deadband","deadband")
    pushPropertyToTable(26, "derivative-constant","")
    pushPropertyToTable(27, "derivative-constant-units","")
    pushPropertyToTable(28, "description","description")
    pushPropertyToTable(29, "description-of-halt","")
    pushPropertyToTable(30, "device-address-binding","")
    pushPropertyToTable(31, "device-type","deviceType")
    pushPropertyToTable(32, "effective-period","")
    pushPropertyToTable(33, "elapsed-active-time","")
    pushPropertyToTable(34, "error-limit","")
    pushPropertyToTable(35, "event-enable","")
    pushPropertyToTable(36, "event-state","")
    pushPropertyToTable(37, "event-type","")
    pushPropertyToTable(38, "exception-schedule","")
    pushPropertyToTable(39, "fault-values","")
    pushPropertyToTable(40, "feedback-value","")
    pushPropertyToTable(41, "file-access-method","")
    pushPropertyToTable(42, "file-size","")
    pushPropertyToTable(43, "file-type","")
    pushPropertyToTable(44, "firmware-revision","")
    pushPropertyToTable(45, "high-limit","highLimit")
    pushPropertyToTable(46, "inactive-text","")
    pushPropertyToTable(47, "in-process","")
    pushPropertyToTable(48, "instance-of","")
    pushPropertyToTable(49, "integral-constant","")
    pushPropertyToTable(50, "integral-constant-units","")
    pushPropertyToTable(51, "issue-confirmed-notifications","")
    pushPropertyToTable(52, "limit-enable","")
    pushPropertyToTable(53, "list-of-group-members","")
    pushPropertyToTable(54, "list-of-object-property-references","")
    pushPropertyToTable(56, "local-date","")
    pushPropertyToTable(57, "local-time","")
    pushPropertyToTable(58, "location","location")
    pushPropertyToTable(59, "low-limit","")
    pushPropertyToTable(60, "manipulated-variable-reference","")
    pushPropertyToTable(61, "maximum-output","")
    pushPropertyToTable(62, "max-apdu-length-accepted","")
    pushPropertyToTable(63, "max-info-frames","")
    pushPropertyToTable(64, "max-master","")
    pushPropertyToTable(65, "max-pres-value","")
    pushPropertyToTable(66, "minimum-off-time","")
    pushPropertyToTable(67, "minimum-on-time","")
    pushPropertyToTable(68, "minimum-output","")
    pushPropertyToTable(69, "min-pres-value","")
    pushPropertyToTable(70, "model-name","")
    pushPropertyToTable(71, "modification-date","")
    pushPropertyToTable(72, "notify-type","")
    pushPropertyToTable(73, "number-of-apdu-retries","")
    pushPropertyToTable(74, "number-of-states","numberOfStates")
    pushPropertyToTable(75, "object-identifier","objectIdentifier")
    pushPropertyToTable(76, "object-list","objectList")
    pushPropertyToTable(77, "object-name","objectName")
    pushPropertyToTable(78, "object-property-reference","")
    pushPropertyToTable(79, "object-type","objectType")
    pushPropertyToTable(80, "optional","optional")
    pushPropertyToTable(81, "out-of-service","outOfService")
    pushPropertyToTable(82, "output-units","")
    pushPropertyToTable(83, "event-parameters","")
    pushPropertyToTable(84, "polarity","polarity")
    pushPropertyToTable(85, "present-value","presentValue")
    pushPropertyToTable(86, "priority","priority")
    pushPropertyToTable(87, "priority-array","priorityArray")
    pushPropertyToTable(88, "priority-for-writing","")
    pushPropertyToTable(89, "process-identifier","")
    pushPropertyToTable(90, "program-change","")
    pushPropertyToTable(91, "program-location","")
    pushPropertyToTable(92, "program-state","")
    pushPropertyToTable(93, "proportional-constant","")
    pushPropertyToTable(94, "proportional-constant-units","")
    pushPropertyToTable(96, "protocol-object-types-supported","")
    pushPropertyToTable(97, "protocol-services-supported","")
    pushPropertyToTable(98, "protocol-version","")
    pushPropertyToTable(99, "read-only","")
    pushPropertyToTable(100, "reason-for-halt","")
    pushPropertyToTable(102, "recipient-list","")
    pushPropertyToTable(103, "reliability","reliability")
    pushPropertyToTable(104, "relinquish-default","")
    pushPropertyToTable(105, "required","required")
    pushPropertyToTable(106, "resolution","resolution")
    pushPropertyToTable(107, "segmentation-supported","")
    pushPropertyToTable(108, "setpoint","setpoint")
    pushPropertyToTable(109, "setpoint-reference","")
    pushPropertyToTable(110, "state-text","stateText")
    pushPropertyToTable(111, "status-flags","")
    pushPropertyToTable(112, "system-status","")
    pushPropertyToTable(113, "time-delay","timeDelay")
    pushPropertyToTable(114, "time-of-active-time-reset","")
    pushPropertyToTable(115, "time-of-state-count-reset","")
    pushPropertyToTable(116, "time-synchronization-recipients","")
    pushPropertyToTable(117, "units","units")
    pushPropertyToTable(118, "update-interval","")
    pushPropertyToTable(119, "utc-offset","")
    pushPropertyToTable(120, "vendor-identifier","")
    pushPropertyToTable(121, "vendor-name","vendorName")
    pushPropertyToTable(122, "vt-classes-supported","")
    pushPropertyToTable(123, "weekly-schedule","")
    pushPropertyToTable(124, "attempted-samples","")
    pushPropertyToTable(125, "average-value","")
    pushPropertyToTable(126, "buffer-size","")
    pushPropertyToTable(127, "client-cov-increment","")
    pushPropertyToTable(128, "cov-resubscription-interval","")
    pushPropertyToTable(130, "event-time-stamps","")
    pushPropertyToTable(131, "log-buffer","")
    pushPropertyToTable(132, "log-device-object-property","")
    pushPropertyToTable(133, "enable","")
    pushPropertyToTable(134, "log-interval","")
    pushPropertyToTable(135, "maximum-value","")
    pushPropertyToTable(136, "minimum-value","")
    pushPropertyToTable(137, "notification-threshold","")
    pushPropertyToTable(139, "protocol-revision","")
    pushPropertyToTable(140, "records-since-notification","")
    pushPropertyToTable(141, "record-count","")
    pushPropertyToTable(142, "start-time","")
    pushPropertyToTable(143, "stop-time","")
    pushPropertyToTable(144, "stop-when-full","")
    pushPropertyToTable(145, "total-record-count","")
    pushPropertyToTable(146, "valid-samples","")
    pushPropertyToTable(147, "window-interval","")
    pushPropertyToTable(148, "window-samples","")
    pushPropertyToTable(149, "maximum-value-timestamp","")
    pushPropertyToTable(150, "minimum-value-timestamp","")
    pushPropertyToTable(151, "variance-value","")
    pushPropertyToTable(152, "active-cov-subscriptions","")
    pushPropertyToTable(153, "backup-failure-timeout","")
    pushPropertyToTable(154, "configuration-files","")
    pushPropertyToTable(155, "database-revision","")
    pushPropertyToTable(156, "direct-reading","")
    pushPropertyToTable(157, "last-restore-time","")
    pushPropertyToTable(158, "maintenance-required","")
    pushPropertyToTable(159, "member-of","")
    pushPropertyToTable(160, "mode","")
    pushPropertyToTable(161, "operation-expected","")
    pushPropertyToTable(162, "setting","")
    pushPropertyToTable(162, "silenced","")
    pushPropertyToTable(164, "tracking-value","")
    pushPropertyToTable(165, "zone-members","")
    pushPropertyToTable(166, "life-safety-alarm-values","")
    pushPropertyToTable(167, "max-segments-accepted","")
    pushPropertyToTable(168, "profile-name","")
    pushPropertyToTable(169, "auto-slave-discovery","")
    pushPropertyToTable(170, "manual-slave-address-binding","")
    pushPropertyToTable(171, "slave-address-binding","")
    pushPropertyToTable(172, "slave-proxy-enable","")    
    pushPropertyToTable(173, "last-notify-record","")
    pushPropertyToTable(174, "schedule-default","")
    pushPropertyToTable(175, "accepted-modes","")
    pushPropertyToTable(176, "adjust-value","")
    pushPropertyToTable(177, "count","")
    pushPropertyToTable(178, "count-before-change","")
    pushPropertyToTable(179, "count-change-time","")
    pushPropertyToTable(180, "cov-period","")
    pushPropertyToTable(181, "input-reference","")
    pushPropertyToTable(182, "limit-monitoring-interval","")
    pushPropertyToTable(183, "logging-object","")
    pushPropertyToTable(184, "logging-record","")
    pushPropertyToTable(185, "prescale","")
    pushPropertyToTable(186, "pulse-rate","")
    pushPropertyToTable(187, "scale","")
    pushPropertyToTable(188, "scale-factor","")
    pushPropertyToTable(189, "update-time","")
    pushPropertyToTable(190, "value-before-change","")
    pushPropertyToTable(191, "value-set","")
    pushPropertyToTable(192, "value-change-time","")
    pushPropertyToTable(193, "align-intervals","")
    pushPropertyToTable(195, "interval-offset","")
    pushPropertyToTable(196, "last-restart-reason","")
    pushPropertyToTable(197, "logging-type","")
    pushPropertyToTable(202, "restart-notification-recipients","")
    pushPropertyToTable(203, "time-of-device-restart","")
    pushPropertyToTable(204, "time-synchronization-interval","")
    pushPropertyToTable(205, "trigger","")
    pushPropertyToTable(206, "utc-time-synchronization-recipients","")
    pushPropertyToTable(207, "node-subtype","")
    pushPropertyToTable(208, "node-type","")
    pushPropertyToTable(209, "structured-object-list","")
    pushPropertyToTable(210, "subordinate-annotations","")
    pushPropertyToTable(211, "subordinate-list","")
    pushPropertyToTable(212, "actual-shed-level","")
    pushPropertyToTable(213, "duty-window","")
    pushPropertyToTable(214, "expected-shed-level","")
    pushPropertyToTable(215, "full-duty-baseline","")
    pushPropertyToTable(218, "requested-shed-level","")
    pushPropertyToTable(219, "shed-duration","")

    pushPropertyToTable(371, "property-list","propertyList")

    pushPropertyToTable(417, "command","command")
    pushPropertyToTable(418, "fd-bbmd-address","fdBBMDAddress")
    pushPropertyToTable(419, "fd-subscription-lifetime","fdSubscriptionLifetime")
    pushPropertyToTable(420, "link-speed","linkSpeed")
    pushPropertyToTable(421, "link-speeds","linkSpeeds")
    pushPropertyToTable(422, "link-speed-autonegotiate","linkSpeedAutonegotiate")

    pushPropertyToTable(508, "additional-reference-ports","additionalReferencePorts")
    pushPropertyToTable(509, "certificate-signing-request-file","certificateSigningRequestFile")
    pushPropertyToTable(510, "command-validation-result","commandValidationResult")
    pushPropertyToTable(511, "issuer-certificate-files","issuerCertificateFiles")

    pushPropertyToTable(4194304, "max-bvlc-length-accepted","maxBvlcLengthAccepted")
    pushPropertyToTable(4194305, "max-npdu-lngth-accepted","maxNpduLengthAccepted")
    pushPropertyToTable(4194306, "operational-certificate-file","operationalCertificateFile")
    pushPropertyToTable(4194307, "current-health","currentHealth")
    pushPropertyToTable(4194308, "sc-connect-wait-timeout","scConnectWaitTimeout")
    pushPropertyToTable(4194309, "sc-direct-connect-accept-enable","scDirectConnectAcceptEnable")
    pushPropertyToTable(4194310, "sc-direct-connect-accept-uris","scDirectConnectAcceptUris")
    pushPropertyToTable(4194311, "sc-direct-connect-binding","scDirectConnectBinding")
    pushPropertyToTable(4194312, "sc-direct-connect-connection-status","scDirectConnectConnectionStatus")
    pushPropertyToTable(4194313, "sc-direct-connect-initiate-enable","scDirectConnectInitiateEnable")
    pushPropertyToTable(4194314, "sc-disconnect-wait-timeout","scDisconnectWaitTimeout")
    pushPropertyToTable(4194315, "sc-failed-connection-requests","scFailedConnectionRequests")
    pushPropertyToTable(4194316, "sc-failover-hub-connection-status","scFailoverHubConnectionStatus")
    pushPropertyToTable(4194317, "sc-failover-hub-uri","scFailoverHubUri")
    pushPropertyToTable(4194318, "sc-hub-connector-state","scHubConnectorState")
    pushPropertyToTable(4194319, "sc-hub-function-accept-uris","scHubFunctionAcceptUris")
    pushPropertyToTable(4194320, "sc-hub-function-binding","scHubFunctionBinding")
    pushPropertyToTable(4194321, "sc-hub-function-connection-status","scHubFunctionConnectionStatus")
    pushPropertyToTable(4194322, "sc-hub-function-enable","scHubFunctionEnable")
    pushPropertyToTable(4194323, "sc-heartbeat-timeout","scHeartbeatTimeout")
    pushPropertyToTable(4194324, "sc-primary-hub-connection-status","scPrimaryHubConnectionStatus")
    pushPropertyToTable(4194325, "sc-primary-hub-uri","scPrimaryHubUri")
    pushPropertyToTable(4194326, "sc-maximum-reconnect-time","scMaximumReconnectTime")
    pushPropertyToTable(4194327, "sc-minimum-reconnect-time","scMinimumReconnectTime")

    /*
    pushPropertyToTable(0, "shed-level-descriptions (220),
    pushPropertyToTable(0, "shed-levels (221),
    pushPropertyToTable(0, "state-description (222),
    pushPropertyToTable(0, "door-alarm-state (226),
    pushPropertyToTable(0, "door-extended-pulse-time (227),
    pushPropertyToTable(0, "door-members (228),
    pushPropertyToTable(0, "door-open-too-long-time (229),
    pushPropertyToTable(0, "door-pulse-time (230),
    pushPropertyToTable(0, "door-status (231),
    pushPropertyToTable(0, "door-unlock-delay-time (232),
    pushPropertyToTable(0, "lock-status (233),
    pushPropertyToTable(0, "masked-alarm-values (234),
    pushPropertyToTable(0, "secured-status (235),
    pushPropertyToTable(0, "absentee-limit (244),
    pushPropertyToTable(0, "access-alarm-events (245),
    pushPropertyToTable(0, "access-doors (246),
    pushPropertyToTable(0, "access-event (247),
    pushPropertyToTable(0, "access-event-authentication-factor (248),
    pushPropertyToTable(0, "access-event-credential (249),
    pushPropertyToTable(0, "access-event-time (250),
    pushPropertyToTable(0, "access-transaction-events (251),
    pushPropertyToTable(0, "accompaniment (252),
    pushPropertyToTable(0, "accompaniment-time (253),
    pushPropertyToTable(0, "activation-time (254),
    pushPropertyToTable(0, "active-authentication-policy (255),
    pushPropertyToTable(0, "assigned-access-rights (256),
    pushPropertyToTable(0, "authentication-factors (257),
    pushPropertyToTable(0, "authentication-policy-list (258),
    pushPropertyToTable(0, "authentication-policy-names (259),
    pushPropertyToTable(0, "authentication-status (260),
    pushPropertyToTable(0, "authorization-mode (261),
    pushPropertyToTable(0, "belongs-to (262),
    pushPropertyToTable(0, "credential-disable (263),
    pushPropertyToTable(0, "credential-status (264),
    pushPropertyToTable(0, "credentials (265),
    pushPropertyToTable(0, "credentials-in-zone (266),
    pushPropertyToTable(0, "days-remaining (267),
    pushPropertyToTable(0, "entry-points (268),
    pushPropertyToTable(0, "exit-points (269),
    pushPropertyToTable(0, "expiration-time (270),
    pushPropertyToTable(0, "extended-time-enable (271),
    pushPropertyToTable(0, "failed-attempt-events (272),
    pushPropertyToTable(0, "failed-attempts (273),
    pushPropertyToTable(0, "failed-attempts-time (274),
    pushPropertyToTable(0, "last-access-event (275),
    pushPropertyToTable(0, "last-access-point (276),
    pushPropertyToTable(0, "last-credential-added (277),
    pushPropertyToTable(0, "last-credential-added-time (278),
    pushPropertyToTable(0, "last-credential-removed (279),
    pushPropertyToTable(0, "last-credential-removed-time (280),
    pushPropertyToTable(0, "last-use-time (281),
    pushPropertyToTable(0, "lockout (282),
    pushPropertyToTable(0, "lockout-relinquish-time (283),
    pushPropertyToTable(0, "max-failed-attempts (285),
    pushPropertyToTable(0, "members (286),
    pushPropertyToTable(0, "muster-point (287),
    pushPropertyToTable(0, "negative-access-rules (288),
    pushPropertyToTable(0, "number-of-authentication-policies (289),
    pushPropertyToTable(0, "occupancy-count (290),
    pushPropertyToTable(0, "occupancy-count-adjust (291),
    pushPropertyToTable(0, "occupancy-count-enable (292),
    pushPropertyToTable(0, "occupancy-lower-limit (294),
    pushPropertyToTable(0, "occupancy-lower-limit-enforced (295),
    pushPropertyToTable(0, "occupancy-state (296),
    pushPropertyToTable(0, "occupancy-upper-limit (297),
    pushPropertyToTable(0, "occupancy-upper-limit-enforced (298),
    pushPropertyToTable(0, "passback-mode (300),
    pushPropertyToTable(0, "passback-timeout (301),
    pushPropertyToTable(0, "positive-access-rules (302),
    pushPropertyToTable(0, "reason-for-disable (303),
    pushPropertyToTable(0, "supported-formats (304),
    pushPropertyToTable(0, "supported-format-classes (305),
    pushPropertyToTable(0, "threat-authority (306),
    pushPropertyToTable(0, "threat-level (307),
    pushPropertyToTable(0, "trace-flag (308),
    pushPropertyToTable(0, "transaction-notification-class (309),
    pushPropertyToTable(0, "user-external-identifier (310),
    pushPropertyToTable(0, "user-information-reference (311),
    pushPropertyToTable(0, "user-name (317),
    pushPropertyToTable(0, "user-type (318),
    pushPropertyToTable(0, "uses-remaining (319),
    pushPropertyToTable(0, "zone-from (320),
    pushPropertyToTable(0, "zone-to (321),
    pushPropertyToTable(0, "access-event-tag (322),
    pushPropertyToTable(0, "global-identifier (323),
    pushPropertyToTable(0, "verification-time (326),
    pushPropertyToTable(0, "backup-and-restore-state (338),
    pushPropertyToTable(0, "backup-preparation-time (339),
    pushPropertyToTable(0, "restore-completion-time (340),
    pushPropertyToTable(0, "restore-preparation-time (341),
    pushPropertyToTable(0, "bit-mask (342),
    pushPropertyToTable(0, "bit-text (343),
    pushPropertyToTable(0, "is-utc (344),
    pushPropertyToTable(0, "group-members (345),
    pushPropertyToTable(0, "group-member-names (346),
    pushPropertyToTable(0, "member-status-flags (347),
    pushPropertyToTable(0, "requested-update-interval (348),
    pushPropertyToTable(0, "covu-period (349),
    pushPropertyToTable(0, "covu-recipients (350),
    pushPropertyToTable(0, "event-message-texts (351),
    pushPropertyToTable(0, "event-message-texts-config (352),
    pushPropertyToTable(0, "event-detection-enable (353),
    pushPropertyToTable(0, "event-algorithm-inhibit (354),
    pushPropertyToTable(0, "event-algorithm-inhibit-ref (355),
    pushPropertyToTable(0, "time-delay-normal (356),
    pushPropertyToTable(0, "reliability-evaluation-inhibit (357),
    pushPropertyToTable(0, "fault-parameters (358),
    pushPropertyToTable(0, "fault-type (359),
    pushPropertyToTable(0, "local-forwarding-only (360),
    pushPropertyToTable(0, "process-identifier-filter (361),
    pushPropertyToTable(0, "subscribed-recipients (362),
    pushPropertyToTable(0, "port-filter (363),
    pushPropertyToTable(0, "authorization-exemptions (364),
    pushPropertyToTable(0, "allow-group-delay-inhibit (365),
    pushPropertyToTable(0, "channel-number (366),
    pushPropertyToTable(0, "control-groups (367),
    pushPropertyToTable(0, "execution-delay (368),
    pushPropertyToTable(0, "last-priority (369),
    pushPropertyToTable(0, "write-status (370),
    pushPropertyToTable(0, "property-list (371),
    pushPropertyToTable(0, "serial-number (372),
    pushPropertyToTable(0, "blink-warn-enable (373),
    pushPropertyToTable(0, "default-fade-time (374),
    pushPropertyToTable(0, "default-ramp-rate (375),
    pushPropertyToTable(0, "default-step-increment (376),
    pushPropertyToTable(0, "egress-time (377),
    pushPropertyToTable(0, "in-progress (378),
    pushPropertyToTable(0, "instantaneous-power (379),
    pushPropertyToTable(0, "lighting-command (380),
    pushPropertyToTable(0, "lighting-command-default-priority (381),
    pushPropertyToTable(0, "max-actual-value (382),
    pushPropertyToTable(0, "min-actual-value (383),
    pushPropertyToTable(0, "power (384),
    pushPropertyToTable(0, "transition (385),
    pushPropertyToTable(0, "egress-active (386),
    pushPropertyToTable(0, "interface-value (387),
    pushPropertyToTable(0, "fault-high-limit (388),
    pushPropertyToTable(0, "fault-low-limit (389),
    pushPropertyToTable(0, "low-diff-limit (390),
    pushPropertyToTable(0, "strike-count (391),
    pushPropertyToTable(0, "time-of-strike-count-reset (392),
    pushPropertyToTable(0, "default-timeout (393),
    pushPropertyToTable(0, "initial-timeout (394),
    pushPropertyToTable(0, "last-state-change (395),
    pushPropertyToTable(0, "state-change-values (396),
    pushPropertyToTable(0, "timer-running (397),
    pushPropertyToTable(0, "timer-state (398),
    pushPropertyToTable(0, "apdu-length (399),
    pushPropertyToTable(0, "ip-address (400),
    pushPropertyToTable(0, "ip-default-gateway (401),
    pushPropertyToTable(0, "ip-dhcp-enable (402),
    pushPropertyToTable(0, "ip-dhcp-lease-time (403),
    pushPropertyToTable(0, "ip-dhcp-lease-time-remaining (404),
    pushPropertyToTable(0, "ip-dhcp-server (405),
    pushPropertyToTable(0, "ip-dns-server (406),
    pushPropertyToTable(0, "bacnet-ip-global-address (407),
    pushPropertyToTable(0, "bacnet-ip-mode (408),
    pushPropertyToTable(0, "bacnet-ip-multicast-address (409),
    pushPropertyToTable(0, "bacnet-ip-nat-traversal (410),
    pushPropertyToTable(0, "ip-subnet-mask (411),
    pushPropertyToTable(0, "bacnet-ip-udp-port (412),
    pushPropertyToTable(0, "bbmd-accept-fd-registrations (413),
    pushPropertyToTable(0, "bbmd-broadcast-distribution-table (414),
    pushPropertyToTable(0, "bbmd-foreign-device-table (415),
    pushPropertyToTable(0, "changes-pending (416),
    pushPropertyToTable(0, "command (417),
    pushPropertyToTable(0, "fd-bbmd-address (418),
    pushPropertyToTable(0, "fd-subscription-lifetime (419),
    pushPropertyToTable(0, "link-speed (420),
    pushPropertyToTable(0, "link-speeds (421),
    pushPropertyToTable(0, "link-speed-autonegotiate (422),
    pushPropertyToTable(0, "mac-address (423),
    pushPropertyToTable(0, "network-interface-name (424),
    pushPropertyToTable(0, "network-number (425),
    pushPropertyToTable(0, "network-number-quality (426),
    pushPropertyToTable(0, "network-type (427),
    pushPropertyToTable(0, "routing-table (428),
    pushPropertyToTable(0, "virtual-mac-address-table (429),
    pushPropertyToTable(0, "command-time-array (430),
    pushPropertyToTable(0, "current-command-priority (431),
    pushPropertyToTable(0, "last-command-time (432),
    pushPropertyToTable(0, "value-source (433),
    pushPropertyToTable(0, "value-source-array (434),
    pushPropertyToTable(0, "bacnet-ipv6-mode (435),
    pushPropertyToTable(0, "ipv6-address (436),
    pushPropertyToTable(0, "ipv6-prefix-length (437),
    pushPropertyToTable(0, "bacnet-ipv6-udp-port (438),
    pushPropertyToTable(0, "ipv6-default-gateway (439),
    pushPropertyToTable(0, "bacnet-ipv6-multicast-address (440),
    pushPropertyToTable(0, "ipv6-dns-server (441),
    pushPropertyToTable(0, "ipv6-auto-addressing-enable (442),
    pushPropertyToTable(0, "ipv6-dhcp-lease-time (443),
    pushPropertyToTable(0, "ipv6-dhcp-lease-time-remaining (444),
    pushPropertyToTable(0, "ipv6-dhcp-server (445),
    pushPropertyToTable(0, "ipv6-zone-index (446),
    pushPropertyToTable(0, "assigned-landing-calls (447),
    pushPropertyToTable(0, "car-assigned-direction (448),
    pushPropertyToTable(0, "car-door-command (449),
    pushPropertyToTable(0, "car-door-status (450),
    pushPropertyToTable(0, "car-door-text (451),
    pushPropertyToTable(0, "car-door-zone (452),
    pushPropertyToTable(0, "car-drive-status (453),
    pushPropertyToTable(0, "car-load (454),
    pushPropertyToTable(0, "car-load-units (455),
    pushPropertyToTable(0, "car-mode (456),
    pushPropertyToTable(0, "car-moving-direction (457),
    pushPropertyToTable(0, "car-position (458),
    pushPropertyToTable(0, "elevator-group (459),
    pushPropertyToTable(0, "energy-meter (460),
    pushPropertyToTable(0, "energy-meter-ref (461),
    pushPropertyToTable(0, "escalator-mode (462),
    pushPropertyToTable(0, "fault-signals (463),
    pushPropertyToTable(0, "floor-text (464),
    pushPropertyToTable(0, "group-id (465),
    pushPropertyToTable(0, "group-mode (467),
    pushPropertyToTable(0, "higher-deck (468),
    pushPropertyToTable(0, "installation-id (469),
    pushPropertyToTable(0, "landing-calls (470),
    pushPropertyToTable(0, "landing-call-control (471),
    pushPropertyToTable(0, "landing-door-status (472),
    pushPropertyToTable(0, "lower-deck (473),
    pushPropertyToTable(0, "machine-room-id (474),
    pushPropertyToTable(0, "making-car-call (475),
    pushPropertyToTable(0, "next-stopping-floor (476),
    pushPropertyToTable(0, "operation-direction (477),
    pushPropertyToTable(0, "passenger-alarm (478),
    pushPropertyToTable(0, "power-mode (479),
    pushPropertyToTable(0, "registered-car-call (480),
    pushPropertyToTable(0, "active-cov-multiple-subscriptions (481),
    pushPropertyToTable(0, "protocol-level (482),
    pushPropertyToTable(0, "reference-port (483),
    pushPropertyToTable(0, "deployed-profile-location (484),
    pushPropertyToTable(0, "profile-location (485),
    pushPropertyToTable(0, "tags (486),
    pushPropertyToTable(0, "subordinate-node-types (487),
    pushPropertyToTable(0, "subordinate-tags (488),
    pushPropertyToTable(0, "subordinate-relationships (489),
    pushPropertyToTable(0, "default-subordinate-relationship (490),
    pushPropertyToTable(0, "represents (491),
    pushPropertyToTable(0, "default-present-value (492),
    pushPropertyToTable(0, "present-stage (493),
    pushPropertyToTable(0, "stages (494),
    pushPropertyToTable(0, "stage-names (495),
    pushPropertyToTable(0, "target-references (496),
    pushPropertyToTable(0, "audit-source-level (497),
    pushPropertyToTable(0, "audit-level (498),
    pushPropertyToTable(0, "audit-notification-recipient (499),
    pushPropertyToTable(0, "audit-priority-filter (500),
    pushPropertyToTable(0, "auditable-operations (501),
    pushPropertyToTable(0, "delete-on-forward (502),
    pushPropertyToTable(0, "maximum-send-delay (503),
    pushPropertyToTable(0, "monitored-objects (504),
    pushPropertyToTable(0, "send-now (505),
    pushPropertyToTable(0, "floor-number (506),
    pushPropertyToTable(0, "device-uuid (507),
    */
}

/** Load the Property IDs in the BACnetPropertyIDs table into the HTML page.
 * 
 * @param table The HTML table to load the BACnetPropertyIDs table into
 * @param data The BACnetPropertyIDs table to load into the HTML table
 */
function loadPropertIDsIntoTable(table, data) {
    for (let element of data) {
        let row = table.insertRow();
        for (key in element) {
          let cell = row.insertCell();
          let text = document.createTextNode(element[key]);
          cell.appendChild(text);
        }
      }
}

/** Create a table header to add to the HTML table.
 *
 * For the BACnet Property IDs, the header names are obtained from the table
 * 'keys' of the BACnetPropertyIDs table.
 * 
 * @param table The HTML table to add a table header to
 * @param data  The header data to add to the HTML table
 */
function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data) {
      let th = document.createElement("th","");
      let text = document.createTextNode(key);
      th.appendChild(text);
      row.appendChild(th);
    }
}

///////////// Code to run when this .js file is loaded in an html file
let htmlTable = document.querySelector("table","")
getPropertyIDs()
let headerData = Object.keys(BACnetPropertyIDs[0]);
generateTableHead(htmlTable, headerData)
loadPropertIDsIntoTable(htmlTable, BACnetPropertyIDs)

