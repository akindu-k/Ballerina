import ballerina/http;
import ballerina/io;

public function main() returns error? {
    // Simulate task details (this will eventually come from Trello or any task system)
    json task = {
        "task_complexity": 2,
        "employee_skill": 3,
        "task_urgency": 2
    };

    // Call the ML model (Flask server) to assign the task
    json assignedTask = check getEmployeeAssignment(task);
    io:println("Assigned Task: ", assignedTask);
}

// Function to call the Flask ML model API to get task assignment
function getEmployeeAssignment(json task) returns json|error {
    // This points to your locally running Flask server
    http:Client mlClient = check new ("http://localhost:5000");
    
    // Send a POST request to the /predict endpoint with task data
    http:Response response = check mlClient->post("/predict", task);
    // Parse the JSON response from Flask with explicit json type
    json result = check response.getJsonPayload();
    return result;
}
