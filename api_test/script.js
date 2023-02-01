// C => Create => POST
// R => Retrieve => GET
// U => Update => PUT/PATCH
// D => Delete => DELETE

// GET Request
// axios.get("http://127.0.0.1:8000/apiV1/status/list/")
//     .then(response => console.log(response))

// axios.get("http://127.0.0.1:8000/apiV1/status/detail/2/")
//     .then(response => console.log(response))

// POST Request
// let status = {
//     user: 1,
//     content: "I am test data!",
//     image: null
// }
// axios.post("http://127.0.0.1:8000/apiV1/status/create/", status, {
//     headers: {
//         "Content-Type": "application/json"
//     }
// })
//     .then(response => console.log(response))
//     .catch(error => console.log(error.message))

// DELETE Request
// axios.delete("http://127.0.0.1:8000/apiV1/status/delete/7/")
//     .then(response => console.log(response))

// PUT Request -> Whole Entity
// PATCH Request -> Just the particular Property
let u_status = {
  content: "I have be updated using PATCH!",
};
axios
  .patch("http://127.0.0.1:8000/apiV1/status/update/8/", u_status, {
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then((response) => console.log(response));
