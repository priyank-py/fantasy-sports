from django.db import models

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
    tournament = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})

