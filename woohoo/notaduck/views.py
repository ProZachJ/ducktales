import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    try:
        data = json.loads(request.body)
        a = request.GET.get('vara')
        a = float(a)
        b = int(request.GET.get('varb'))

        resp = {}
        for key in data:
            math = data[key] / data['q']
            resp[key] = {'type': type(
                data[key]).__name__, 'value': data[key], 'math': math, 'math-type': type(math).__name__}
        resp['a'] = {'type': type(a).__name__, 'value': a}
        resp['b'] = {'type': type(b).__name__, 'value': b}
        othervar = a / b
        resp['othervar'] = {'type': type(othervar).__name__, 'value': othervar}
    except:
        print('nope')
    return JsonResponse(resp)


@csrf_exempt
def messages(request):
    try:
        newmessage = json.loads(request.body)
        old_message = request.session.get('old_message', {
            'user': 'default', 'message_id': 1, 'message': 'This is the first message'})
        if old_message['message_id'] == newmessage['message_id']:
            return JsonResponse({'Error': 'Duplicate message id'})
        else:
            old_message = newmessage
            request.session['old_message'] = old_message
    except:
        print("Something went wrong")
    return JsonResponse(old_message)


@csrf_exempt
def bids(request):
    try:
        bid = json.loads(request.body)
        current_high_bid = request.session.get(
            'high_bid', {'user': 'starting bid', 'bid': 0.00})
        if bid['bid'] < current_high_bid['bid']:
            return JsonResponse({'Message': 'Your bid is too low'})
        else:
            current_high_bid = bid
            request.session['high_bid'] = current_high_bid
    except:
        print("Something went wrong")
    return JsonResponse({"High Bid": current_high_bid})


@csrf_exempt
def ratings(request):
    total_ratings = {}
    try:
        newrating = json.loads(request.body)
        currentratings = request.session.get('ratings', {})
        if newrating['book'] in currentratings:
            for rating in currentratings[newrating['book']]:
                if rating['user'] == newrating['user']:
                    msg = 'You have already submitted a review for ' + \
                        newrating['book']
                    return JsonResponse({'Error': msg})
            currentratings[newrating['book']].append({
                'rating': newrating['rating'], 'user': newrating['user']})
            request.session['ratings'] = currentratings
        else:
            currentratings[newrating['book']] = [{
                'rating': newrating['rating'], 'user': newrating['user']}]
            request.session['ratings'] = currentratings
        for book in currentratings:
            for rating in currentratings[book]:
                if book in total_ratings:
                    total_ratings[book] = total_ratings[book] + \
                        rating['rating']
                else:
                    total_ratings[book] = rating['rating']
            total_ratings[book] = total_ratings[book] / \
                len(currentratings[book])
        winning_score = 0
        winner = {}
        for score in total_ratings:
            if total_ratings[score] > winning_score:
                winning_score = total_ratings[score]
                winner = score
        total_ratings['highest_rated'] = winner
    except:
        print("Something went wrong")
    return JsonResponse(total_ratings)


@csrf_exempt
def blindbids(request):
    try:
        bid = json.loads(request.body)
        bids = request.session.get('bids', [])
        bid_order = request.session.get('bid_order', {})
        bid_num = len(bids) + 1
        bids.append(bid['bid'])
        bid_order[bid_num] = bid['user']
        request.session['bids'] = bids
        request.session['bid_order'] = bid_order
        print(bids)
    except:
        print("Something went wrong")
    response = bid['user'] + \
        " thank you for your bid of $" + str(bid['bid'])
    return JsonResponse({"mesage": response})


def whowon(request):
    response = ''
    try:
        bids = request.session.get('bids', [])
        bid_order = request.session.get('bid_order', {})
        print(bids)
        print(bid_order)
        sorted_bids = sorted(bids)
        largest_bid = sorted_bids[len(sorted_bids) - 1]
        temp = 0
        for bid in bids:
            temp = temp + 1
            if largest_bid == bid:
                response = bid_order[str(temp)] + \
                    " has the winning bid! of $" + str(bid)
    except:
        print("Something went wrong")
    return JsonResponse({"winner": response})
