// C => Create => POST
// R => Retrieve => GET
// U => Update => PUT/PATCH
// D => Delete => DELETE

// 1

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
// let u_status = {
//   content: "I have be updated using PATCH!",
// };
// axios
//   .patch("http://127.0.0.1:8000/apiV1/status/update/8/", u_status, {
//     headers: {
//       "Content-Type": "application/json",
//     },
//   })
//   .then((response) => console.log(response));

// 2

document.getElementById("myForm").addEventListener("submit", handleSubmit);
document.getElementById("image").addEventListener("change", handleImage);

let myImage = null;

function handleImage(e) {
  myImage = e.target.files[0];
  //console.log(myImage);
}

function handleSubmit(e) {
  e.preventDefault();
  let user = document.getElementById("user").value;
  let content = document.getElementById("content").value;
  let form_data = new FormData();
  form_data.append("user", user);
  form_data.append("content", content);
  form_data.append("image", myImage);

  // for (var [key, value] of form_data.entries()) {
  //     console.log(key, ": ", value);
  // }
  axios
    .post("http://127.0.0.1:8000/apiV1/status/", form_data, {
      header: {
        "Content-Type": "multipart/form-data",
      },
    })
    .then((response) => console.log(response));
}
