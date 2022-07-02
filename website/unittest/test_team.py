import unittest

@views.route('/team', methods=['GET', 'POST'])
@login_required
def team():
    if request.method == 'POST':
        Games = request.form.getlist('game')
        Platform = request.form.getlist('platform')
        tteam = request.form.get('name')
        Description = request.form.get('deskripsi')
  
        with open("a+") as file:
            data = {}
            data['Team'] = []
            data['Team'].append({
                "Game": Games,
                "Platform": Platform, 
                "Team Name": tteam,
                "Description": Description
            })
            file.write(json.dumps(data, indent=2))
            file.write("\n")
    return render_template("team.html", user=current_user)