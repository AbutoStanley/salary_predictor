async function predict() {

    const data = {
        experience_level: document.getElementById("experience_level").value,
        employment_type: document.getElementById("employment_type").value,
        company_size: document.getElementById("company_size").value,
        work_year: parseInt(document.getElementById("work_year").value),
        remote_ratio: parseInt(document.getElementById("remote_ratio").value),
        residence_grouped: document.getElementById("residence_grouped").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    const formatted = Number(result.predicted_salary_usd)
        .toLocaleString("en-US", { style: "currency", currency: "USD" });

    document.getElementById("result").innerText = formatted;
}