from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route('/')
def home():
    def generate_lotto_numbers():
        return sorted(random.sample(range(1, 46), 6))
    def count_common_elements(list1, list2):
        set1, set2 = set(list1), set(list2)
        return sum(elem in set2 for elem in set1)
    
    name="조성현"
    lotto=[16,18,22,43,32,11]
    random_lotto=generate_lotto_numbers()
    common_count= count_common_elements(lotto, random_lotto)
    common_count=6;
    context={
        "name":name,
        "lotto" :lotto,
        "random_lotto":random_lotto,
        "common_count": common_count,
    }
    return render_template('index.html', data=context)


@app.route('/mypage')
def mypage():
    return 'This is Mypage!'
    
@app.route('/movie')
def movie():
    query = request.args.get('query')
    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}"
    )
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    return render_template('movie.html', data=movie_list)

@app.route('/askbyday')
def askbyday():
    if request.args.get('askday'):
        askday = request.args.get('askday')
    else :
        askday='20230601'
    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={askday}"
    )
    rjson = res.json()
    movie_list = rjson["boxOfficeResult"]["weeklyBoxOfficeList"]
    
    return render_template('askbyday.html',data=movie_list)

if __name__ == '__main__':  
    app.run(debug=True)