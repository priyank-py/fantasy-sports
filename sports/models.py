from django.db import models
from django.utils.translation import ugettext_lazy as _

FORMAT_CHOICES = (
    ('t20', 'T-20'),
    ('odi', 'ODI'),
    ('test', ('Test')),
)

class Cricket(models.Model):
    date = models.DateTimeField(_("Match Date/Time"), auto_now=False, auto_now_add=False)
    venue = models.CharField(_("Venue"), max_length=50)
    match_format = models.CharField(_("Format"), max_length=15, choices=FORMAT_CHOICES)
    tournament_name = models.CharField(_("Tournament Name"), max_length=80) 
    team1 = models.CharField(_("Team 1"), max_length=50)
    team2 = models.CharField(_("Team 2"), max_length=50)
    class Meta:
        verbose_name = _("Cricket")
        verbose_name_plural = _("Crickets")

    def __str__(self):
        return f'{self.tournament_name} Match {self.team1} vs {self.team2}'

    def get_absolute_url(self):
        return reverse("Cricket_detail", kwargs={"pk": self.pk})


class Team(models.Model):
    name = models.CharField(_("Team Name"), max_length=50)
    tournament = models.ForeignKey(Cricket, verbose_name=_("Tournament"), on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})


def upload_to(self, instance, filename):
    return f'Players_Image/{instance.name}/{filename}'

PLAYER_TYPES= (
    ('batsman', 'Batsman'),
    ('allrounder', 'All-Rounder'),
    ('wicketkeeper', 'Wicket Keeper'),
    ('baller', 'Baller')
)

BATTING_STYLE = (
    ('right_handed', 'Right-Handed'),
    ('left_handed', 'Right-Handed')
)

BALLING_STYLE = (
    ('right_arm_fast','Right-arm fast'),
    ('right_arm_medium_fast', 'Right-arm medium fast'),
    ('right_arm_medium', 'Right-arm medium'),
    ('left_arm_fast', 'Left-arm fast'),
    ('left_arm_medium_fast', 'Left-arm medium fast'),
    ('off_break_right', 'Off break (right-arm)'),
    ('leg_break_right', 'Leg break (right-arm)'),
    ('slow_left_arm', 'Slow left-arm orthodox'),
    ('slow_left_arm_wrist_spin', 'Slow left-arm wrist spin')
)

class CricketPlayerT20(models.Model):
    team = models.ForeignKey(Team , verbose_name=_("Team"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    photo = models.ImageField(_("Photo"), upload_to=None, height_field=None, width_field=None, max_length=None)
    player_type = models.CharField(_("Player Type"), max_length=15, choices=PLAYER_TYPES)
    matches = models.IntegerField(_("Matches"), blank=True, null=True)
    innings = models.IntegerField(_("Innings"), blank=True, null=True)
    batting_style = models.CharField(_("Batting Style"), max_length=50, choices=BATTING_STYLE, blank=True, null=True)
    career_runs = models.IntegerField(_("Career Runs"), blank=True, null=True)
    catches = models.IntegerField(_("Catches"), blank=True, null=True)
    bat_average = models.FloatField(_("Batting Average"), blank=True, null=True) 
    wickets = models.IntegerField(_("Wickets"), blank=True, null=True)
    balling_style = models.CharField(_("Balling Style"), max_length=50, choices=BATTING_STYLE, blank=True, null=True)
    ball_average = models.FloatField(_("Ball Average"), blank=True, null=True)
    highest_score = models.SmallIntegerField(_("Highest Score"), blank=True, null=True)
    hightest_wicket = models.SmallIntegerField(_("Highest Wicket"), blank=True, null=True)
    fifties = models.SmallIntegerField(_("50s"), blank=True, null=True)
    hundreds = models.SmallIntegerField(_("100s"), blank=True, null=True)


    class Meta:
        verbose_name = _("Cricket Player T-20")
        verbose_name_plural = _("Cricket Players T-20")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CricketPlayerT20_detail", kwargs={"pk": self.pk})

class CricketPlayerODI(CricketPlayerT20):
    class Meta:
        verbose_name = _("Cricket Player ODI")
        verbose_name_plural = _("Cricket Players ODI")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("CricketPlayerODI_detail", kwargs={"pk": self.pk})

class CricketPlayerTest(CricketPlayerT20):
    class Meta:
        verbose_name = _('Cricket Player Test')
        verbose_name_plural = _('Cricket Players Test')
    
    def __str__(self):
        self.name

    def get_absolute_url(self):
        return reverse("CricketPlayerTest_detail", kwargs={"pk": self.pk})
        

class CricketPlayerIPL(CricketPlayerT20):
    class Meta:
        verbose_name = _('Cricket Player IPL')
        verbose_name_plural = _('Cricket Players IPL')
    
    def __str__(self):
        self.name
    
    def get_absolute_url(self):
        return reverse("CricketPlayerIPL_detail", kwargs={"pk": self.pk})
    