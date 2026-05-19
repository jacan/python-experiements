import json
import random
from datetime import UTC, datetime, timedelta
from pathlib import Path

SERVICES = [
    "gateway",
    "auth",
    "payment",
    "inventory",
    "invoice",
    "frontend",
    "audit",
    "notification",
    "shipping",
    "orders",
]

NORMAL_MESSAGES = {
    "gateway": [
        "Request received",
        "Request forwarded",
        "Connection established",
    ],
    "auth": [
        "Token validated",
        "Session refreshed",
        "MFA challenge completed",
    ],
    "payment": [
        "Payment processed",
        "Card authorized",
        "Settlement completed",
    ],
    "inventory": [
        "Inventory reserved",
        "Stock updated",
        "Warehouse synchronized",
    ],
    "invoice": [
        "Invoice generated",
        "PDF rendered",
        "Invoice archived",
    ],
    "frontend": [
        "Page rendered",
        "Asset cache hit",
        "User session active",
    ],
    "audit": [
        "Audit event recorded",
        "Compliance rule validated",
        "Access event logged",
    ],
    "notification": [
        "Email dispatched",
        "Webhook delivered",
        "Push notification queued",
    ],
    "shipping": [
        "Shipment created",
        "Tracking updated",
        "Carrier accepted shipment",
    ],
    "orders": [
        "Order created",
        "Order finalized",
        "Order status updated",
    ],
}

ERROR_MESSAGES = {
    "payment": [
        "Database timeout",
        "Card rejected",
        "Payment processor unavailable",
    ],
    "inventory": [
        "Inventory item missing",
        "Warehouse synchronization failed",
        "Reservation conflict detected",
    ],
    "invoice": [
        "Spooler unable to create invoice",
        "PDF rendering failed",
        "Invoice template corrupted",
    ],
    "frontend": [
        "CDN unreachable",
        "JavaScript bundle missing",
        "API request timeout",
    ],
    "audit": [
        "Audit persistence failed",
        "Transaction missing MFA",
        "Compliance service unavailable",
    ],
    "notification": [
        "SMTP server unreachable",
        "Webhook delivery failed",
        "Push queue overflow",
    ],
    "shipping": [
        "Carrier API unavailable",
        "Tracking synchronization failed",
        "Shipment label generation failed",
    ],
    "orders": [
        "Order state invalid",
        "Order locking conflict",
        "Order persistence timeout",
    ],
    "gateway": [
        "Upstream service unavailable",
        "Connection pool exhausted",
        "SIGKILL received",
    ],
    "auth": [
        "JWT signature invalid",
        "MFA provider timeout",
        "Session lookup failed",
    ]
}

def generate_logs(count: int = 5000):
    logs = []

    current = datetime(2026, 1, 1, tzinfo=UTC)

    for _ in range(count):
        current += timedelta(seconds=random.randint(1, 30))

        service = random.choice(SERVICES)

        # Normal distribution
        level = random.choices(
            ["INFO", "WARNING", "ERROR"],
            weights=[80, 15, 5],
        )[0]

        # Simulate cascading failures
        if random.random() < 0.02:
            cascade_services = ["gateway", "payment", "invoice", "frontend"]

            for cascade_service in cascade_services:
                logs.append(
                    {
                        "timestamp": current.isoformat().replace("+00:00", "Z"),
                        "service": cascade_service,
                        "level": "ERROR",
                        "message": random.choice(
                            get_error_messaeg_safely(service)
                        ),
                    }
                )

            continue

        if level == "INFO":
            message = random.choice(NORMAL_MESSAGES[service])

        elif level == "WARNING":
            message = random.choice(
                [
                    "Retry threshold exceeded",
                    "Latency above baseline",
                    "Temporary degradation detected",
                    "Slow downstream response",
                ]
            )

        else:
            message = random.choice(get_error_messaeg_safely(service))

        logs.append(
            {
                "timestamp": current.isoformat().replace("+00:00", "Z"),
                "service": service,
                "level": level,
                "message": message,
            }
        )

    return logs

def get_error_messaeg_safely(service_name: str) -> list[str] | str:
    return ERROR_MESSAGES.get(service_name, "unknown service")


def main():
    project_root = Path(__file__).resolve().parent.parent

    output_path = project_root / "sample_data" / "logs_big.json"

    output_path.parent.mkdir(exist_ok=True)

    logs = generate_logs(5000)

    with open(output_path, "w") as file:
        json.dump(logs, file, indent=2)

    print(f"Generated {len(logs)} log entries")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()