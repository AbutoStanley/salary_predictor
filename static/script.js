document.getElementById("salaryForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const data = {
        work_year: parseInt(document.getElementById("work_year").value),
        experience_level: document.getElementById("experience_level").value,
        employment_type: document.getElementById("employment_type").value,
        remote_ratio: parseInt(document.getElementById("remote_ratio").value),
        company_size: document.getElementById("company_size").value,
        residence_grouped: document.getElementById("residence_grouped").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        "Estimated Salary: $" + result.predicted_salary_usd.toLocaleString();
});