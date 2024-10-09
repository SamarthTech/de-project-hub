// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DeProjectHub {
    // Struct to hold project information
    struct Project {
        string projectName;
        address owner;
        string repositoryLink;
    }

    // Mapping to store all projects by an ID
    mapping(uint256 => Project) public projects;

    // Counter for project IDs
    uint256 public projectCount = 0;

    // Event triggered when a new project is added
    event ProjectAdded(uint256 indexed projectId, string projectName, address indexed owner, string repositoryLink);

    // Function to add a new project
    function addProject(string memory _projectName, string memory _repositoryLink) public {
        // Increment the project count for unique IDs
        projectCount++;

        // Store the new project
        projects[projectCount] = Project(_projectName, msg.sender, _repositoryLink);

        // Emit event for the added project
        emit ProjectAdded(projectCount, _projectName, msg.sender, _repositoryLink);
    }

    // Function to get details of a project by its ID
    function getProject(uint256 _projectId) public view returns (string memory, address, string memory) {
        Project memory project = projects[_projectId];
        return (project.projectName, project.owner, project.repositoryLink);
    }
}
