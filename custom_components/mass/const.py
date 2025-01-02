"""Constants for Music Assistant Component."""

import logging

DOMAIN = "mass"
DOMAIN_EVENT = f"{DOMAIN}_event"

DEFAULT_NAME = "Music Assistant"

ATTR_IS_GROUP = "is_group"
ATTR_GROUP_MEMBERS = "group_members"
ATTR_GROUP_PARENTS = "group_parents"
ATTR_ACTIVE_QUEUE = "active_queue"
ATTR_ACTIVE_GROUP = "active_group"
ATTR_QUEUE_ITEMS = "items_in_queue"
ATTR_QUEUE_INDEX = "queue_index"
ATTR_GROUP_LEADER = "group_leader"
ATTR_MASS_PLAYER_ID = "mass_player_id"
ATTR_MASS_PLAYER_TYPE = "mass_player_type"
ATTR_MEDIA_ID = "media_id"
ATTR_MEDIA_TYPE = "media_type"
ATTR_RADIO_MODE = "radio_mode"
ATTR_STREAM_TITLE = "stream_title"

CONF_OPENAI_AGENT_ID = "openai_agent_id"
CONF_ASSIST_AUTO_EXPOSE_PLAYERS = "expose_players_assist"
CONF_PRE_ANNOUNCE_TTS = "pre_announce_tts"

SERVICE_PLAY_MEDIA_ADVANCED = "play_media"

LOGGER = logging.getLogger(__package__)
