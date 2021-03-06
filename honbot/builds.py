import logparse
from .models import Builds, Matches, PlayerMatches
from django.shortcuts import redirect
import datetime
from error import error
from django.shortcuts import render_to_response
import json


def build_view(request, match_id):
    match = Matches.objects.filter(match_id=match_id).values()
    if match.exists():
        builds = Builds.objects.filter(match_id=match_id).values()
        if builds.exists():
            match = match[0]
            match['date'] = datetime.datetime.strptime(
                str(match['date']), '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=1)
            players = PlayerMatches.objects.filter(
                match=match_id).order_by('position')
            for build in builds:
                build['json'] = json.loads(build['json'])
            return render_to_response('build.html', {'builds': builds, 'match': match, 'players': players})
        else:
            if logparse.download(match_id, match[0]['replay_url']):
                if logparse.parse(match_id):
                    return build_view(request, match_id)
                else:
                    return error(request, "The chat logs had trouble somewhere. We all have bad days sometimes.")
            else:
                return error(request, "Match replay failed to download. It could be too old (28 days), too new, or S2 hates you")
    else:
        return redirect('/match/' + match_id + '/')
