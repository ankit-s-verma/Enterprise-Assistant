import type { Ticket } from "../types";

export function buildTicket(data: any): Ticket {
  return {
    id: data.ticket_id,
    issue: data.issue,
    status: data.status,
  };
}

export function buildTicketResponse(
  data: any,
  ticket: Ticket | null
): string {
  const responses: string[] = [];

  if (data.status) {
    responses.push(
      `${ticket?.id} is currently ${data.status}.`
    );
  }

  if (data.issue) {
    responses.push(
      `The issue for ticket ${ticket?.id} is "${data.issue}".`
    );
  }

  return responses.join(" ");
}