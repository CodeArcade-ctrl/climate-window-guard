# Climate Window Guard

**Get a clear Home Assistant sensor when a window is open while heating or cooling is actively running.**

Choose one window contact sensor and one climate entity. The integration creates a binary sensor that turns on only when the contact is open and the climate entity reports `heating` or `cooling` as its current action. Use it in an automation to pause a thermostat or send yourself a notification.

## Install with HACS

1. In Home Assistant, open **HACS → Integrations**.
2. Open the **⋮** menu and choose **Custom repositories**.
3. Add `https://github.com/CodeArcade-ctrl/climate-window-guard` and choose **Integration**.
4. Install **Climate Window Guard**, then restart Home Assistant.
5. Open **Settings → Devices & services → Add integration**, search for **Climate Window Guard**, and choose the window and climate entities.

HACS custom repositories must be added by each user. This repository is not yet part of the HACS default catalog.

## What it creates

- **Heating/cooling with window open**: an alert binary sensor for use in dashboards and automations.
- A setup form that filters for window contacts and climate entities.
- English and Dutch setup and entity names.

The sensor checks source states every 15 seconds. It does not control the climate device, close windows, or contact an external service. If a climate integration does not report the current `hvac_action`, this sensor cannot detect active heating or cooling for that entity.

## Privacy and requirements

All calculations run in Home Assistant. No account, network service, or extra Python dependency is required. Requires Home Assistant Core 2025.1 or newer and a window binary sensor plus a climate entity.

## License

MIT. See [LICENSE](LICENSE).
