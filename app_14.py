from flask import Flask, request, jsonify

app = Flask(__name__)

githubPublicData = {
	"username": 'ankit123',
	"fullName": 'Ankit Kumar',
	"email": 'ankit@gmail.com',
	"repositories": 24,
	"gists": 12,
	"joinedOn": 'Sep 2018',
}

# Get profile URL
def getProfileUrl(githubPublicData):
    profileUrl = f"https://github.com/{githubPublicData['username']}"
    return {
        'profileUrl': profileUrl
    }

@app.route("/github-profile", methods=["GET"])
def github_profile():
    result = getProfileUrl(githubPublicData)
    return jsonify(result)

# Public Email
def getpublicEmail(githubPublicData):
    return {
        'publicEmail': githubPublicData['email']
    }

@app.route("/github-public-email", methods=["GET"])
def github_public_email():
    result = getpublicEmail(githubPublicData)
    return jsonify(result)

# Repos Count
def getReposCount(githubPublicData):
    return {
        'reposCount': githubPublicData['repositories']
    }

@app.route("/github-repos-count", methods=["GET"])
def github_repos_count():
    result = getReposCount(githubPublicData)
    return jsonify(result) 

# Gists Count
def getGistsCount(githubProfileData):
    return {
        'gistsCount': githubPublicData['gists']
    }

@app.route("/github-gists-count", methods=["GET"])
def github_gists_count():
    result = getGistsCount(githubPublicData)
    return jsonify(result)

# User Bio
def getUserBio(githubPublicData):
    return {
        "fullName": githubPublicData['fullName'],
        "joinedOn": githubPublicData['joinedOn'],
        "email": githubPublicData['email']
    }

@app.route("/github-user-bio", methods=["GET"])
def github_user_bio():
    result = getUserBio(githubPublicData)
    return jsonify(result)

# Repository URL
def getRepoUrl(githubPublicData):
    username = githubPublicData['username']
    repoUrl = f"https://github.com/{username}"
    return repoUrl    

@app.route("/github-repo-url", methods=["GET"])
def github_repo_url():
    repoName = request.args.get("repoName", "")
    repoUrl = getRepoUrl(githubPublicData)
    result = f"{repoUrl}/{repoName}"
    return jsonify({ "repoUrl": result })

if __name__ == "__main__":
   app.run() 
