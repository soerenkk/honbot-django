from django.db import models
from datetime import datetime


class Matches(models.Model):
    match_id = models.PositiveIntegerField(
        primary_key=True, null=False, unique=True, db_index=True)
    date = models.DateTimeField(blank=True, null=False)
    replay_url = models.URLField(max_length=120, default="", null=True)
    realtime = models.CharField(max_length=10, default="")
    mode = models.CharField(max_length=10, default="", db_index=True)
    map_used = models.CharField(max_length=30, default="")
    major = models.PositiveSmallIntegerField(default=0)
    minor = models.PositiveSmallIntegerField(default=0)
    revision = models.PositiveSmallIntegerField(default=0)
    build = models.PositiveSmallIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True, default=datetime.now)

    class Meta:
        ordering = ['-match_id']


class PlayerMatches(models.Model):
    player_id = models.PositiveIntegerField(default=0, db_index=True)
    match = models.ForeignKey(Matches, null=False, db_index=True)
    deaths = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    apm = models.FloatField(default=0)
    cs = models.PositiveSmallIntegerField(default=0)
    buybacks = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveSmallIntegerField(default=0)
    razed = models.PositiveSmallIntegerField(default=0)
    triplekill = models.PositiveSmallIntegerField(default=0)
    doublekill = models.PositiveSmallIntegerField(default=0)
    quadkill = models.PositiveSmallIntegerField(default=0)
    annihilation = models.PositiveSmallIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    gold_spent = models.PositiveIntegerField(default=0)
    exp_denied = models.PositiveIntegerField(default=0)
    bgold = models.PositiveIntegerField(default=0)
    secsdead = models.PositiveIntegerField(default=0)
    gpm = models.FloatField(default=0)
    bdmg = models.PositiveSmallIntegerField(default=0)
    herodmg = models.PositiveIntegerField(default=0)
    xpm = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    mmr_change = models.FloatField(default=0)
    goldlost2death = models.PositiveSmallIntegerField(default=0)
    denies = models.PositiveSmallIntegerField(default=0)
    hero = models.PositiveSmallIntegerField(default=0)
    kills = models.PositiveSmallIntegerField(default=0)
    consumables = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    nickname = models.TextField(max_length=25, default="")
    level = models.PositiveSmallIntegerField(default=0)
    wards = models.PositiveSmallIntegerField(default=0)
    team = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveSmallIntegerField(default=0)
    items = models.CharField(max_length=50, default="")
    mode = models.CharField(max_length=10, default="", db_index=True)
    date = models.DateTimeField(db_index=True, blank=True, null=True)


class PlayerMatchesCasual(models.Model):
    player_id = models.PositiveIntegerField(default=0, db_index=True)
    match = models.ForeignKey(Matches, null=False, db_index=True)
    deaths = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    apm = models.FloatField(default=0)
    cs = models.PositiveSmallIntegerField(default=0)
    buybacks = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveSmallIntegerField(default=0)
    razed = models.PositiveSmallIntegerField(default=0)
    triplekill = models.PositiveSmallIntegerField(default=0)
    doublekill = models.PositiveSmallIntegerField(default=0)
    quadkill = models.PositiveSmallIntegerField(default=0)
    annihilation = models.PositiveSmallIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    gold_spent = models.PositiveIntegerField(default=0)
    exp_denied = models.PositiveIntegerField(default=0)
    bgold = models.PositiveIntegerField(default=0)
    secsdead = models.PositiveIntegerField(default=0)
    gpm = models.FloatField(default=0)
    bdmg = models.PositiveSmallIntegerField(default=0)
    herodmg = models.PositiveIntegerField(default=0)
    xpm = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    mmr_change = models.FloatField(default=0)
    goldlost2death = models.PositiveSmallIntegerField(default=0)
    denies = models.PositiveSmallIntegerField(default=0)
    hero = models.PositiveSmallIntegerField(default=0)
    kills = models.PositiveSmallIntegerField(default=0)
    consumables = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    nickname = models.TextField(max_length=25, default="")
    level = models.PositiveSmallIntegerField(default=0)
    wards = models.PositiveSmallIntegerField(default=0)
    team = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveSmallIntegerField(default=0)
    items = models.CharField(max_length=50, default="")
    mode = models.CharField(max_length=10, default="", db_index=True)
    date = models.DateTimeField(db_index=True, blank=True, null=True)


class PlayerMatchesPublic(models.Model):
    player_id = models.PositiveIntegerField(default=0, db_index=True)
    match = models.ForeignKey(Matches, null=False, db_index=True)
    deaths = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    apm = models.FloatField(default=0)
    cs = models.PositiveSmallIntegerField(default=0)
    buybacks = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveSmallIntegerField(default=0)
    razed = models.PositiveSmallIntegerField(default=0)
    triplekill = models.PositiveSmallIntegerField(default=0)
    doublekill = models.PositiveSmallIntegerField(default=0)
    quadkill = models.PositiveSmallIntegerField(default=0)
    annihilation = models.PositiveSmallIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    gold_spent = models.PositiveIntegerField(default=0)
    exp_denied = models.PositiveIntegerField(default=0)
    bgold = models.PositiveIntegerField(default=0)
    secsdead = models.PositiveIntegerField(default=0)
    gpm = models.FloatField(default=0)
    bdmg = models.PositiveSmallIntegerField(default=0)
    herodmg = models.PositiveIntegerField(default=0)
    xpm = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    mmr_change = models.FloatField(default=0)
    goldlost2death = models.PositiveSmallIntegerField(default=0)
    denies = models.PositiveSmallIntegerField(default=0)
    hero = models.PositiveSmallIntegerField(default=0)
    kills = models.PositiveSmallIntegerField(default=0)
    consumables = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    nickname = models.TextField(max_length=25, default="")
    level = models.PositiveSmallIntegerField(default=0)
    wards = models.PositiveSmallIntegerField(default=0)
    team = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveSmallIntegerField(default=0)
    items = models.CharField(max_length=50, default="")
    mode = models.CharField(max_length=10, default="", db_index=True)
    date = models.DateTimeField(db_index=True, blank=True, null=True)


class PlayerIcon(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, db_index=True)
    avatar = models.URLField(max_length=300, default="")
    updated = models.DateTimeField(auto_now=True, default=0)


class PlayerHistory(models.Model):
    player_id = models.PositiveIntegerField(default=0, db_index=True)
    history = models.TextField(default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    mode = models.CharField(max_length=10, default="", db_index=True)


class PlayerStats(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, db_index=True)
    nickname = models.CharField(max_length=30, default="", db_index=True)
    updated = models.DateTimeField(auto_now=True, default=0)
    cccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    razed = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0, db_index=True)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
    aassists = models.FloatField(default=0)
    ks3 = models.PositiveIntegerField(default=0)
    ks4 = models.PositiveIntegerField(default=0)
    ks5 = models.PositiveIntegerField(default=0)
    ks6 = models.PositiveIntegerField(default=0)
    ks7 = models.PositiveIntegerField(default=0)
    ks8 = models.PositiveIntegerField(default=0)
    ks9 = models.PositiveIntegerField(default=0)
    ks10 = models.PositiveIntegerField(default=0)
    ks15 = models.PositiveIntegerField(default=0)
    bloodlust = models.PositiveIntegerField(default=0)
    doublekill = models.PositiveIntegerField(default=0)
    triplekill = models.PositiveIntegerField(default=0)
    quadkill = models.PositiveIntegerField(default=0)
    annihilation = models.PositiveIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    humiliation = models.PositiveIntegerField(default=0)
    nemesis = models.PositiveIntegerField(default=0)
    retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return "/player/%s/" % self.nickname


class PlayerStatsCasual(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    nickname = models.CharField(max_length=30, default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    cccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    razed = models.PositiveIntegerField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
    aassists = models.FloatField(default=0)
    ks3 = models.PositiveIntegerField(default=0)
    ks4 = models.PositiveIntegerField(default=0)
    ks5 = models.PositiveIntegerField(default=0)
    ks6 = models.PositiveIntegerField(default=0)
    ks7 = models.PositiveIntegerField(default=0)
    ks8 = models.PositiveIntegerField(default=0)
    ks9 = models.PositiveSmallIntegerField(default=0)
    ks10 = models.PositiveSmallIntegerField(default=0)
    ks15 = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveIntegerField(default=0)
    doublekill = models.PositiveIntegerField(default=0)
    triplekill = models.PositiveIntegerField(default=0)
    quadkill = models.PositiveIntegerField(default=0)
    annihilation = models.PositiveIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    humiliation = models.PositiveIntegerField(default=0)
    nemesis = models.PositiveIntegerField(default=0)
    retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)


class PlayerStatsPublic(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    nickname = models.CharField(max_length=30, default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    cccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0, null=True)
    razed = models.PositiveIntegerField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
    aassists = models.FloatField(default=0)
    ks3 = models.PositiveIntegerField(default=0)
    ks4 = models.PositiveIntegerField(default=0)
    ks5 = models.PositiveIntegerField(default=0)
    ks6 = models.PositiveIntegerField(default=0)
    ks7 = models.PositiveIntegerField(default=0)
    ks8 = models.PositiveIntegerField(default=0)
    ks9 = models.PositiveSmallIntegerField(default=0)
    ks10 = models.PositiveSmallIntegerField(default=0)
    ks15 = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveIntegerField(default=0)
    doublekill = models.PositiveIntegerField(default=0)
    triplekill = models.PositiveIntegerField(default=0)
    quadkill = models.PositiveIntegerField(default=0)
    annihilation = models.PositiveIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    humiliation = models.PositiveIntegerField(default=0)
    nemesis = models.PositiveIntegerField(default=0)
    retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)


class PlayerHeroStats(models.Model):
    nickname = models.CharField(max_length=30, default="")
    data = models.TextField(default="")
    hero_id = models.SmallIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, default=0)
    mode = models.CharField(max_length=10, default="rnk")


class Chat(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, db_index=True)
    json = models.TextField(default="")


class Builds(models.Model):
    match_id = models.PositiveIntegerField(null=False, default=1, db_index=True)
    hero = models.PositiveSmallIntegerField(default=0, db_index=True)
    json = models.TextField(default="")
    nickname = models.CharField(max_length=30, default="")
    position = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    mmr = models.PositiveIntegerField(default=0)
    lvl1 = models.PositiveSmallIntegerField(default=0)
    lvl2 = models.PositiveSmallIntegerField(default=0)
    lvl3 = models.PositiveSmallIntegerField(default=0)
    lvl4 = models.PositiveSmallIntegerField(default=0)
    lvl5 = models.PositiveSmallIntegerField(default=0)
    lvl6 = models.PositiveSmallIntegerField(default=0)
    lvl7 = models.PositiveSmallIntegerField(default=0)
    lvl8 = models.PositiveSmallIntegerField(default=0)
    lvl9 = models.PositiveSmallIntegerField(default=0)
    lvl10 = models.PositiveSmallIntegerField(default=0)
    lvl11 = models.PositiveSmallIntegerField(default=0)
    lvl12 = models.PositiveSmallIntegerField(default=0)
    lvl13 = models.PositiveSmallIntegerField(default=0)
    lvl14 = models.PositiveSmallIntegerField(default=0)
    lvl15 = models.PositiveSmallIntegerField(default=0)
    lvl16 = models.PositiveSmallIntegerField(default=0)
    lvl17 = models.PositiveSmallIntegerField(default=0)
    lvl18 = models.PositiveSmallIntegerField(default=0)
    lvl19 = models.PositiveSmallIntegerField(default=0)
    lvl20 = models.PositiveSmallIntegerField(default=0)
    lvl21 = models.PositiveSmallIntegerField(default=0)
    lvl22 = models.PositiveSmallIntegerField(default=0)
    lvl23 = models.PositiveSmallIntegerField(default=0)
    lvl24 = models.PositiveSmallIntegerField(default=0)
    lvl25 = models.PositiveSmallIntegerField(default=0)


class PlayerCount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)


class MatchCount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)


class PlayerMatchCount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)


class APICount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)

class Heroes(models.Model):
    hero_id = models.PositiveSmallIntegerField(primary_key=True, unique=True, db_index=True)
    disp_name = models.TextField(default="")
    description = models.TextField(default="", null=True)
    primaryattribute = models.TextField(default="")
    attacktype = models.TextField(default="")
    team = models.TextField(default="")
    updated = models.DateTimeField(auto_now=True, default=datetime.now)

    def get_absolute_url(self):
        return "/hero/%s/" % self.disp_name

class HeroUse(models.Model):
    date = models.DateField(db_index=True)
    hero_id = models.PositiveSmallIntegerField(default=0, db_index=True)
    popularity = models.PositiveSmallIntegerField(default=0)
    usage = models.PositiveIntegerField(default=0)

class HeroData(models.Model):
    hero_id = models.PositiveSmallIntegerField(primary_key=True, unique=True, db_index=True)
    disp_name = models.TextField(default="")
    cli_name = models.CharField(default="", max_length=120, db_index=True)
    category = models.TextField(default="")
    difficulty = models.FloatField(default=0)
    solorating = models.FloatField(default=0)
    junglerating = models.FloatField(default=0)
    carryrating = models.FloatField(default=0)
    supportrating = models.FloatField(default=0)
    initiatorrating = models.FloatField(default=0)
    gankerating = models.FloatField(default=0)
    pusherrating = models.FloatField(default=0)
    rangedrating = models.FloatField(default=0)
    meleerating = models.FloatField(default=0)
    movespeed = models.PositiveSmallIntegerField(default=0)
    turnrate = models.PositiveSmallIntegerField(default=0)
    maxhealth = models.PositiveSmallIntegerField(default=0)
    healthregen = models.FloatField(default=0)
    manaregen = models.FloatField(default=0)
    maxmana = models.PositiveSmallIntegerField(default=0)
    armor = models.FloatField(default=0)
    magicarmor = models.FloatField(default=0)
    attackduration = models.PositiveSmallIntegerField(default=0)
    attackactiontime = models.PositiveSmallIntegerField(default=0)
    attackcooldown = models.PositiveSmallIntegerField(default=0)
    attackdamagemin = models.PositiveSmallIntegerField(default=0)
    attackdamagemax = models.PositiveSmallIntegerField(default=0)
    attacknumanims = models.PositiveSmallIntegerField(default=0)
    attackrange = models.PositiveSmallIntegerField(default=0)
    attacktype = models.TextField(default="")
    aggrorange = models.PositiveSmallIntegerField(default=0)
    sightrangeday = models.PositiveSmallIntegerField(default=0)
    sightrangenight = models.PositiveSmallIntegerField(default=0)
    wanderrange = models.PositiveSmallIntegerField(default=0)
    primaryattribute = models.TextField(default="")
    strength = models.PositiveSmallIntegerField(default=0)
    strengthperlevel = models.FloatField(default=0)
    agility = models.PositiveSmallIntegerField(default=0)
    agilityperlevel = models.FloatField(default=0)
    intelligence = models.PositiveSmallIntegerField(default=0)
    intelligenceperlevel = models.FloatField(default=0)
    calcattackspeed = models.FloatField(default=0)
    attackspeedpersec = models.FloatField(default=0)
    effectivearmor = models.FloatField(default=0)
    health = models.FloatField(default=0)
    mana = models.FloatField(default=0)
    ability1 = models.TextField(default="")
    ability2 = models.TextField(default="")
    ability3 = models.TextField(default="")
    ability4 = models.TextField(default="")


class MasterRanked(models.Model):
    super_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    nickname = models.CharField(max_length=30, default="")
    standing = models.PositiveSmallIntegerField(default=0)
    account_type = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=50, default="")
    rank = models.CharField(max_length=50, default="")
    rnk_games_played = models.PositiveIntegerField(default=0)
    rnk_wins = models.PositiveIntegerField(default=0)
    rnk_losses = models.PositiveIntegerField(default=0)
    rnk_concedes = models.PositiveIntegerField(default=0)
    rnk_concedevotes = models.PositiveIntegerField(default=0)
    rnk_buybacks = models.PositiveIntegerField(default=0)
    rnk_discos = models.PositiveIntegerField(default=0)
    rnk_kicked = models.PositiveIntegerField(default=0)
    rnk_amm_team_count = models.PositiveIntegerField(default=0)
    rnk_herokills = models.PositiveIntegerField(default=0)
    rnk_herodmg = models.PositiveIntegerField(default=0)
    rnk_heroexp = models.PositiveIntegerField(default=0)
    rnk_herokillsgold = models.PositiveIntegerField(default=0)
    rnk_heroassists = models.PositiveIntegerField(default=0)
    rnk_deaths = models.PositiveIntegerField(default=0)
    rnk_goldlost2death = models.PositiveIntegerField(default=0)
    rnk_teamcreepdmg = models.PositiveIntegerField(default=0)
    rnk_teamcreepexp = models.PositiveIntegerField(default=0)
    rnk_teamcreepgold = models.PositiveIntegerField(default=0)
    rnk_neutralcreepkills = models.PositiveIntegerField(default=0)
    rnk_neutralcreepdmg = models.PositiveIntegerField(default=0)
    rnk_neutralcreepexp = models.PositiveIntegerField(default=0)
    rnk_neutralcreepgold = models.PositiveIntegerField(default=0)
    rnk_bdmg = models.PositiveIntegerField(default=0)
    rnk_bdmgexp = models.PositiveIntegerField(default=0)
    rnk_razed = models.PositiveIntegerField(default=0)
    rnk_bgold = models.PositiveIntegerField(default=0)
    rnk_denies = models.PositiveIntegerField(default=0)
    rnk_exp_denied = models.PositiveIntegerField(default=0)
    rnk_gold = models.PositiveIntegerField(default=0)
    rnk_gold_spent = models.PositiveIntegerField(default=0)
    rnk_exp = models.PositiveIntegerField(default=0)
    rnk_actions = models.PositiveIntegerField(default=0)
    rnk_secs = models.PositiveIntegerField(default=0)
    rnk_consumables = models.PositiveIntegerField(default=0)
    rnk_wards = models.PositiveIntegerField(default=0)
    rnk_level = models.PositiveIntegerField(default=0)
    rnk_level_exp = models.PositiveIntegerField(default=0)
    rnk_min_exp = models.PositiveIntegerField(default=0)
    rnk_max_exp = models.PositiveIntegerField(default=0)
    rnk_time_earning_exp = models.PositiveIntegerField(default=0)
    rnk_bloodlust = models.PositiveIntegerField(default=0)
    rnk_doublekill = models.PositiveIntegerField(default=0)
    rnk_triplekill = models.PositiveIntegerField(default=0)
    rnk_quadkill = models.PositiveIntegerField(default=0)
    rnk_annihilation = models.PositiveSmallIntegerField(default=0)
    rnk_ks3 = models.PositiveIntegerField(default=0)
    rnk_ks4 = models.PositiveIntegerField(default=0)
    rnk_ks5 = models.PositiveIntegerField(default=0)
    rnk_ks6 = models.PositiveIntegerField(default=0)
    rnk_ks7 = models.PositiveIntegerField(default=0)
    rnk_ks8 = models.PositiveIntegerField(default=0)
    rnk_ks9 = models.PositiveIntegerField(default=0)
    rnk_ks10 = models.PositiveIntegerField(default=0)
    rnk_ks15 = models.PositiveIntegerField(default=0)
    rnk_smackdown = models.PositiveIntegerField(default=0)
    rnk_humiliation = models.PositiveIntegerField(default=0)
    rnk_nemesis = models.PositiveIntegerField(default=0)
    rnk_retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    discos = models.PositiveIntegerField(default=0)
    possible_discos = models.PositiveIntegerField(default=0)
    games_played = models.PositiveIntegerField(default=0)
    total_games_played = models.PositiveIntegerField(default=0)
    total_discos = models.PositiveIntegerField(default=0)
    acc_secs = models.PositiveIntegerField(default=0)
    acc_games_played = models.PositiveIntegerField(default=0)
    acc_discos = models.PositiveIntegerField(default=0)
    cs_secs = models.PositiveIntegerField(default=0)
    cs_games_played = models.PositiveIntegerField(default=0)
    cs_discos = models.PositiveIntegerField(default=0)
    unrnk_games_played = models.PositiveIntegerField(default=0)
    unrnk_discos = models.PositiveIntegerField(default=0)
    mid_games_played = models.PositiveIntegerField(default=0)
    mid_discos = models.PositiveIntegerField(default=0)
    rift_games_played = models.PositiveIntegerField(default=0)
    rift_discos = models.PositiveIntegerField(default=0)
    last_activity = models.DateField(default=0)
    create_date = models.DateField(default=0)
    favHero1 = models.CharField(max_length=20, default="")
    favHero1Time = models.FloatField(default=0)
    favHero1_2 = models.CharField(max_length=20, default="")
    favHero2 = models.CharField(max_length=20, default="")
    favHero2Time = models.FloatField(default=0)
    favHero2_2 = models.CharField(max_length=20, default="")
    favHero3 = models.CharField(max_length=20, default="")
    favHero3Time = models.FloatField(default=0)
    favHero3_2 = models.CharField(max_length=20, default="")
    favHero4 = models.CharField(max_length=20, default="")
    favHero4Time = models.FloatField(default=0)
    favHero4_2 = models.CharField(max_length=20, default="")
    favHero5 = models.CharField(max_length=20, default="")
    favHero5Time = models.FloatField(default=0)
    favHero5_2 = models.CharField(max_length=20, default="")
    dice_tokens = models.PositiveSmallIntegerField(default=0)
    slot_id = models.PositiveSmallIntegerField(default=0)
    selected_upgrades = models.TextField(default="")
    timestamp = models.TextField(default="")
    matchIds = models.TextField(default="")
    k_d_a = models.TextField(default="")
    avgGameLength = models.FloatField(default="")
    avgXP_min = models.FloatField(default="")
    avgDenies = models.FloatField(default="")
    avgCreepKills = models.FloatField(default="")
    avgNeutralKills = models.FloatField(default="")
    avgActions_min = models.FloatField(default="")
    avgWardsUsed = models.FloatField(default="")
    vested_threshold = models.PositiveSmallIntegerField(default=0)


class PlayerBrackets(models.Model):
    mmr_bracket = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    maxkills = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    minkills = models.FloatField(default=0)
    stdkills = models.FloatField(default=0)
    maxassists = models.FloatField(default=0)
    aassists = models.FloatField(default=0)
    minassists = models.FloatField(default=0)
    stdassists = models.FloatField(default=0)
    maxdeaths = models.FloatField(default=0)
    adeaths = models.FloatField(default=0)
    mindeaths = models.FloatField(default=0)
    stddeaths = models.FloatField(default=0)
    atime = models.FloatField(default=0)
    maxactionsmin = models.FloatField(default=0)
    aactionsmin = models.FloatField(default=0)
    minactionsmin = models.FloatField(default=0)
    stdactionsmin = models.FloatField(default=0)
    maxcs = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    mincs = models.FloatField(default=0)
    stdcs = models.FloatField(default=0)
    maxdenies = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    mindenies = models.FloatField(default=0)
    stddenies = models.FloatField(default=0)
    maxwards = models.FloatField(default=0)
    awards = models.FloatField(default=0)
    minwards = models.FloatField(default=0)
    stdwards = models.FloatField(default=0)
    maxxpm = models.FloatField(default=0)
    axpm = models.FloatField(default=0)
    minxpm = models.FloatField(default=0)
    stdxpm = models.FloatField(default=0)
    maxgpm = models.FloatField(default=0)
    agpm = models.FloatField(default=0)
    mingpm = models.FloatField(default=0)
    stdgpm = models.FloatField(default=0)
    count = models.PositiveIntegerField(default=0)
