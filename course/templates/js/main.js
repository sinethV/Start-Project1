const staffData = [
    { staffNo: "S3250", name: "Robert Chin", position: "Supervisor", salary: 32000, branch: "B002 - City Center Plaza, Seattle, WA 98122" },
    { staffNo: "S2250", name: "Sally Adams", position: "Manager", salary: 48000, branch: "B004 - 16-14th Avenue, Seattle, WA 98128" },
    { staffNo: "S1500", name: "Tom Daniels", position: "Manager", salary: 46000, branch: "B001 - 8 Jefferson Way, Portland, OR 97201" },
    { staffNo: "S0415", name: "Art Peters", position: "Manager", salary: 41000, branch: "B003 - 14-8th Avenue, New York, NY 10012" },
    { staffNo: "S0010", name: "Mary Martinez", position: "Manager", salary: 50000, branch: "B002 - City Center Plaza, Seattle, WA 98122" },
    { staffNo: "S0003", name: "Sally Adams", position: "Assistant", salary: 30000, branch: "B001 - 8 Jefferson Way, Portland, OR 97201" }
];


let selectedStaff = [];

function renderTable(data) {
    const tbody = document.getElementById('staffTableBody');
    tbody.innerHTML = '';
    data.forEach(staff => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><input type="checkbox" onchange="updateSelection(this, '${staff.staffNo}')"></td>
            <td>${staff.staffNo}</td>
            <td>${staff.name}</td>
            <td>${staff.position}</td>
            <td>${staff.salary}</td>
            <td>${staff.branch}</td>
        `;
        tbody.appendChild(row);
    });
    updateSelectedCount();
}

function updateSelection(checkbox, staffNo) {
    if (checkbox.checked) {
        selectedStaff.push(staffNo);
    } else {
        selectedStaff = selectedStaff.filter(no => no !== staffNo);
    }
    updateSelectedCount();
}

function updateSelectedCount() {
    const count = selectedStaff.length;
    document.getElementById('selectedCount').textContent = `${count} of ${staffData.length} selected`;
}

function searchStaff() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const filteredData = staffData.filter(staff => 
        staff.name.toLowerCase().includes(searchTerm) || 
        staff.position.toLowerCase().includes(searchTerm) || 
        staff.staffNo.toLowerCase().includes(searchTerm)
    );
    renderTable(filteredData);
}

function performAction() {
    const action = document.getElementById('actionSelect').value;
    if (action && selectedStaff.length > 0) {
        alert(`Performing ${action} on staff with STAFFNO: ${selectedStaff.join(', ')}`);
        // Add your logic here for promoting, demoting, or updating salary
    } else {
        alert('Please select an action and at least one staff member.');
    }
}

// Initial render
renderTable(staffData);