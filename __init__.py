import random
import json

from flask import Flask, request, jsonify, render_template, make_response, redirect, url_for
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

status = {"The Service is Online!"}

assignlist_post_arg = reqparse.RequestParser()
assignsingle_post_arg = reqparse.RequestParser()
assignsingle_post_arg.add_argument("controlgrouppercentage", type=float, help="Provide the desired percentage for allocation in the Control Group arm. Range 0.0-1.0", required=False)
assignlist_post_arg.add_argument("controlgrouppercentage", type=float, help="Provide the desired percentage for allocation in the Control Group arm. Range 0.0-1.0")
assignlist_post_arg.add_argument("blocksize", type=int, help="Provide the desired block_size. It must be an int divisible by the number of Study groups and smaller than the overall num of participants", required=True)
assignlist_post_arg.add_argument("participantsnumber", type=int, help="Provide the NUMBER OF THE PARTICIPANTS", required=True)
#assignlist_post_arg.add_argument("participantsids", required=True, action="append")

#print("Request Parser Details:")
#print(f"Arguments: {assignsingle_post_arg.args}")

@app.route("/", methods=["GET", "POST"])
def homeless():
    return redirect(url_for('home'))

@app.route("/randomizationservice", methods=["GET", "POST"])
def home():
    return render_template("dashboard.html")

@app.route("/randomizationservice/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/randomizationservice/checkservicestatus", methods=["GET", "POST"])
def servicestatus():
    return render_template("checkservicestatus.html")

@app.route("/randomizationservice/singleparticipant", methods=["GET", "POST"])
def singleparticipant():
    return render_template("assignsingleparticipant.html")

@app.route("/randomizationservice/listofparticipants", methods=["GET", "POST"])
def listofparticipants():
    return render_template("listofparticipants.html")


class StatusCheck(Resource):
    def get(self):
        return make_response(render_template("checkservicestatusresults.html", response=status), {'Content-Type': 'text/html'})


api.add_resource(StatusCheck, "/randomizationservice/statuscheck")


class AssignSingleParticipant(Resource):
    def post(self):
        print("Reached AssignSingleParticipant")
        #print(assignsingle_post_arg)
        mylist = ["Control Group Arm", "Intervention Group Arm"]
        print(mylist)
        print("Here 1")
        
        args = request.form.get("controlgrouppercentage")
        #print(control_group_percentage1)
        #print("data21 = request.get_json")
        #args = request.get_json()
        #args = json.loads(request.data, strict=False)
        print("data21 is ", args)
        #print("Here 2.5")
        #percentage = data21['controlgrouppercentage']
        #print("percentage = data21['controlgrouppercentage']", percentage)
        #control_group_percentage = data21.get('controlgrouppercentage')
        #print("Here 2.8")
        #print("Here 3")
        #print("The control is ", control_group_percentage)
        #print("Here 4")
        #args = assignsingle_post_arg.parse_args()
        #print("float(args) is....", float(args))
        print("Hello")
        #print(args['controlgrouppercentage'])
        if not args:
            args = 0.5
            print(args)
            #return {"assigned": random.sample(mylist, 1)}
        
        percents = float(args)
        #percents = float(args['controlgrouppercentage'])
        print(percents)
        if percents == 1.0:
            return {"assigned": mylist[0]}

        arg100 = percents*100
        print(arg100)

        perc = arg100 / (100 - arg100)
        print(perc)

        calcweight = random.choices(mylist, weights=[perc, 1], k=1)
        print("the assignment group is: ", calcweight)
        return make_response(render_template("assignsingleparticipantresults.html", response=calcweight), {'Content-Type': 'text/html'})


api.add_resource(AssignSingleParticipant, "/randomizationservice/assignsingleparticipant/")


class AssignListOfParticipants(Resource):
    def post(self):
        mylist = ["Control Group Arm", "Intervention Group Arm"]
        #args = assignlist_post_arg.parse_args()
        #print("Parsed args are:", args)
        percents = request.form.get("controlgrouppercentage")
        #percents = args['controlgrouppercentage']
        print("Percent in str: ", percents)
        #block_size = args['blocksize']
        block_size = request.form.get("blocksize")
        print("Block size in str: ", block_size)
        #participants = args['participantsids']
        #print("Participant's ids in str: ", participants)
        #participants = args['participantsnumber']
        participants = request.form.get("participantsnumber")
        print("Participant's ids in str: ", participants)
        #json_bit = list(map(lambda element: json.loads(element.replace("'", '"')), participants))
        #print("Participant's ids List converted to dictionary: ", participants)

        if not percents:
            distributed = distribute_elements_in_slots(int(participants), len(mylist), int(block_size))
            print(distributed)
        else:
            flexibility = [float(percents) * 100, 100 - (float(percents) * 100)]
            distributed = distribute_elements_in_slots(int(participants), len(mylist), int(block_size), flexibility)
            print(distributed)

        counter = 1
        id_counter = 1
        json_bit = [{"id": w+1, "assigned": mylist[distributed[w]], "block_id": (w // 10)+1} for w in range(int(participants))]
        #print(json_bit)
        for i in json_bit:
            print(i)
            #json_bit[counter - 1]["id"] = counter
         #   json_bit[counter-1]["assigned"] = mylist[distributed[counter]]
          #  json_bit[counter-1]["block_id"] = id_counter
           # if (counter % 10) == 0:
            #    id_counter = id_counter + 1
            #counter = counter + 1

        #print(json_bit)
        return make_response(render_template("listofparticipantsresults.html", response=json_bit),200,{'Content-Type': 'text/html'})
        #return jsonify(json_bit)


api.add_resource(AssignListOfParticipants, "/randomizationservice/assignlistofparticipants/")


def distribute_elements_in_slots(total, slots, block_size, pct=None):
    # Compute proportional distribution by given percentages.
    if pct is None:
        pct = [50, 50]

    if (total % block_size) == 0:
        block_num = total / block_size
    else:
        block_num = (total // block_size) + 1

    distr = [block_size * pct[i] / 100 for i in range(slots)]
    # Truncate each position and store the difference in a new list.
    solid = [int(elem) for elem in distr]
    short = [distr[i] - solid[i] for i in range(slots)]
    print(distr)
    print(solid)
    print(short)

    # allocate leftovers
    leftover = int(round(sum(short)))
    print(leftover)
    # For each unallocated item,
    #   find the neediest slot, and put an extra there.
    for i in range(leftover):
        shortest = short.index(max(short))
        solid[shortest] += 1
        short[shortest] = 0
        print("Added 1 to slot", shortest)

    print(solid)
    print(block_num)
    print(block_size)
    randomlist = []
    for k in range(0, int(block_num)):
        c = solid[0]
        d = solid[1]
        for i in range(0, block_size):
            x = random.randint(0, 1)
            if x == 0 and c > 0:
                randomlist.append(x)
                c = c - 1
            elif x == 1 and d > 0:
                randomlist.append(x)
                d = d - 1
            else:
                if d == 0 and c > 0:
                    randomlist.append(0)
                    c = c - 1
                if c == 0 and d > 0:
                    randomlist.append(1)
                    d = d - 1
    print("exit")
    return randomlist


if __name__ == "__main__":
    app.run(debug=True)