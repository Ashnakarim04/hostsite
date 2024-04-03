{/* <script>
        document.addEventListener("DOMContentLoaded", function () {
            // Get the form element
            var form = document.querySelector("form");
          
            // Add a submit event listener to the form
            form.addEventListener("submit", function (event) {
              // Get the values from the input fields
              var companyName = document.querySelector("#name").value;
              var jobName = document.querySelector("#jname").value;
              var salary = document.querySelector("#salary").value;
          
              // Check if company name and job name are in capital letters
              if (!isUpperCase(companyName)) {
                alert("Company name must be in capital letters.");
                event.preventDefault();
                return;
              }
          
              if (!isUpperCase(jobName)) {
                alert("Job name must be in capital letters.");
                event.preventDefault();
                return;
              }
          
              // Check if salary is a number and above 1000
              if (isNaN(parseFloat(salary)) || parseFloat(salary) <= 1000) {
                alert("Salary should be a number above 1000.");
                event.preventDefault();
                return;
              }
            });
          
            // Function to check if a string is in uppercase
            function isUpperCase(str) {
              return str === str.toUpperCase();
            }
          });
    </script> */}