
export function countOfficial(user, setOfficial) {
    // https://codeforces.com is being proxyed
    fetch(`/api/user.rating?handle=${user}`
    ,{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
      else return {'result': [1,1,1] };
    })
    .then((myJson) => {
      setOfficial(myJson.result.length);
    });

  }

export function listRegistered(contestId) {
    // fetch(`/group/6VlO0zus3c/contestRegistrants/${contestId}`, {
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'Accept': 'application/json'
    //     }
    // })
    // .then((response) => {
    //     console.log(response);
    // });
}
//   def list_registered(contest_id):
//       result = r.get(f"https://codeforces.com/group/6VlO0zus3c/contestRegistrants/{contest_id}")
  
//       soup = S(result.text, features="lxml")
//       soup = soup.find("table", attrs={'class': 'registrants'})
//       links =  soup.find_all("a", href=re.compile(r"^/profile"))
//       return [l.text for l in links]
  