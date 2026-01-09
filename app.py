from flask import Flask, request, jsonify
from resume_matcher import match_resumes

app=Flask(__name__)

@app.route("/match",methods=["POST"])
def match():
    data=request.get_json()
    job_description=data["job_description"]
    resumes=data["resumes"]
    
    if not job_description or not resumes:
        return jsonify({"error: Invalid Input"}),400
    
    scores=match_resumes(job_description,resumes)

    response=[]
    for i, score in enumerate(scores):
        response.append({
            "resume_id":i+1,
            "match_score":f"{score}%"
        })

    response = sorted(response, key=lambda x: x["match_score"], reverse=True)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)