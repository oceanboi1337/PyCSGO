import enum

class Offsets(enum.IntEnum):
	anim_overlays = 0x2990
	clientstate_choked_commands = 0x4d30
	clientstate_delta_ticks = 0x174
	clientstate_last_outgoing_command = 0x4d2c
	clientstate_net_channel = 0x9c
	convar_name_hash_table = 0x301a0
	dwClientState = 0x59f19c
	dwClientState_GetLocalPlayer = 0x180
	dwClientState_IsHLTV = 0x4d48
	dwClientState_Map = 0x28c
	dwClientState_MapDirectory = 0x188
	dwClientState_MaxPlayer = 0x388
	dwClientState_PlayerInfo = 0x52c0
	dwClientState_State = 0x108
	dwClientState_ViewAngles = 0x4d90
	dwEntityList = 0x4e0102c
	dwForceAttack = 0x322ee98
	dwForceAttack2 = 0x322eea4
	dwForceBackward = 0x322eee0
	dwForceForward = 0x322eed4
	dwForceJump = 0x52bcd88
	dwForceLeft = 0x322ee50
	dwForceRight = 0x322ee5c
	dwGameDir = 0x63ae00
	dwGameRulesProxy = 0x5330594
	dwGetAllClasses = 0xe0cfa4
	dwGlobalVars = 0x59ee60
	dwGlowObjectManager = 0x535bad0
	dwInput = 0x525e600
	dwInterfaceLinkList = 0x99cf84
	dwLocalPlayer = 0xdeb99c
	dwMouseEnable = 0x523a260
	dwMouseEnablePtr = 0x523a230
	dwPlayerResource = 0x322d1d0
	dwRadarBase = 0x5237b04
	dwSensitivity = 0xdefbb8
	dwSensitivityPtr = 0xdefbb8
	dwSetClanTag = 0x8dab0
	dwViewMatrix = 0x4df1e74
	dwWeaponTable = 0x525f6dc
	dwWeaponTableIndex = 0x326c
	dwYawPtr = 0xdef948
	dwZoomSensitivityRatioPtr = 0xdf53b8
	dwbSendPackets = 0xdd2d2
	dwppDirect3DDevice9 = 0xa62c0
	find_hud_element = 0x346f26c0
	force_update_spectator_glow = 0x3db90a
	interface_engine_cvar = 0x3fa9c
	is_c4_owner = 0x3e9120
	m_bDormant = 0xed
	m_bIsLocalPlayer = 0x3628
	m_flSpawnTime = 0x103c0
	m_pStudioHdr = 0x2950
	m_pitchClassPtr = 0x523a158
	m_yawClassPtr = 0xdef948
	model_ambient_min = 0x5a1194
	set_abs_angles = 0x1e8fc0
	set_abs_origin = 0x1e8e00
	cs_gamerules_data = 0x0
	m_ArmorValue = 0x117cc
	m_Collision = 0x320
	m_CollisionGroup = 0x474
	m_Local = 0x2fcc
	m_MoveType = 0x25c
	m_OriginalOwnerXuidHigh = 0x31d4
	m_OriginalOwnerXuidLow = 0x31d0
	m_SurvivalGameRuleDecisionTypes = 0x1328
	m_SurvivalRules = 0xd00
	m_aimPunchAngle = 0x303c
	m_aimPunchAngleVel = 0x3048
	m_angEyeAnglesX = 0x117d0
	m_angEyeAnglesY = 0x117d4
	m_bBombDefused = 0x29c0
	m_bBombPlanted = 0x9a5
	m_bBombTicking = 0x2990
	m_bFreezePeriod = 0x20
	m_bGunGameImmunity = 0x9990
	m_bHasDefuser = 0x117dc
	m_bHasHelmet = 0x117c0
	m_bInReload = 0x32b5
	m_bIsDefusing = 0x997c
	m_bIsQueuedMatchmaking = 0x74
	m_bIsScoped = 0x9974
	m_bIsValveDS = 0x7c
	m_bSpotted = 0x93d
	m_bSpottedByMask = 0x980
	m_bStartedArming = 0x3400
	m_bUseCustomAutoExposureMax = 0x9d9
	m_bUseCustomAutoExposureMin = 0x9d8
	m_bUseCustomBloomScale = 0x9da
	m_clrRender = 0x70
	m_dwBoneMatrix = 0x26a8
	m_fAccuracyPenalty = 0x3340
	m_fFlags = 0x104
	m_flC4Blow = 0x29a0
	m_flCustomAutoExposureMax = 0x9e0
	m_flCustomAutoExposureMin = 0x9dc
	m_flCustomBloomScale = 0x9e4
	m_flDefuseCountDown = 0x29bc
	m_flDefuseLength = 0x29b8
	m_flFallbackWear = 0x31e0
	m_flFlashDuration = 0x10470
	m_flFlashMaxAlpha = 0x1046c
	m_flLastBoneSetupTime = 0x2928
	m_flLowerBodyYawTarget = 0x9adc
	m_flNextAttack = 0x2d80
	m_flNextPrimaryAttack = 0x3248
	m_flSimulationTime = 0x268
	m_flTimerLength = 0x29a4
	m_hActiveWeapon = 0x2f08
	m_hBombDefuser = 0x29c4
	m_hMyWeapons = 0x2e08
	m_hObserverTarget = 0x339c
	m_hOwner = 0x29dc
	m_hOwnerEntity = 0x14c
	m_hViewModel = 0x3308
	m_iAccountID = 0x2fd8
	m_iClip1 = 0x3274
	m_iCompetitiveRanking = 0x1a84
	m_iCompetitiveWins = 0x1b88
	m_iCrosshairId = 0x11838
	m_iDefaultFOV = 0x333c
	m_iEntityQuality = 0x2fbc
	m_iFOV = 0x31f4
	m_iFOVStart = 0x31f8
	m_iGlowIndex = 0x10488
	m_iHealth = 0x100
	m_iItemDefinitionIndex = 0x2fba
	m_iItemIDHigh = 0x2fd0
	m_iMostRecentModelBoneCounter = 0x2690
	m_iObserverMode = 0x3388
	m_iShotsFired = 0x103e0
	m_iState = 0x3268
	m_iTeamNum = 0xf4
	m_lifeState = 0x25f
	m_nBombSite = 0x2994
	m_nFallbackPaintKit = 0x31d8
	m_nFallbackSeed = 0x31dc
	m_nFallbackStatTrak = 0x31e4
	m_nForceBone = 0x268c
	m_nModelIndex = 0x258
	m_nTickBase = 0x3440
	m_nViewModelIndex = 0x29d0
	m_rgflCoordinateFrame = 0x444
	m_szCustomName = 0x304c
	m_szLastPlaceName = 0x35c4
	m_thirdPersonViewAngles = 0x31e8
	m_vecOrigin = 0x138
	m_vecVelocity = 0x114
	m_vecViewOffset = 0x108
	m_viewPunchAngle = 0x3030
	m_zoomLevel = 0x33e0
