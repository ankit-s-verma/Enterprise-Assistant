import type { Employee } from "../types/index";

export function buildEmployee(data: any): Employee {
  return {
    id: String(data.employee_id),
    name: data.employee_name,
    designation: data.designation,
    department: data.department,
    email: data.email,
    phone: data.phone_no,
  };
}

export function buildEmployeeResponse(
  data: any,
  employee: Employee | null
): string {
  const responses: string[] = [];

  if (data.name) {
    responses.push(`${data.name}.`);
  }

  if (data.phone) {
    responses.push(
      `${employee?.name}'s phone number is ${data.phone}.`
    );
  }

  if (data.email) {
    responses.push(
      `${employee?.name}'s email address is ${data.email}.`
    );
  }

  if (data.department) {
    responses.push(
      `${employee?.name} works in the ${data.department} department.`
    );
  }

  if (data.designation) {
    responses.push(
      `${employee?.name}'s designation is ${data.designation}.`
    );
  }

  return responses.join(" ");
}