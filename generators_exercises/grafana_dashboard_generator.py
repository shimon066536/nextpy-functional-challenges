"""
grafana_dashboard_generator.py

Creates an example Grafana dashboard using grafanalib.
Useful for infrastructure automation and monitoring visualization.
"""

from grafanalib.core import (
    Dashboard, TimeSeries, GaugePanel,
    Target, GridPos,
    OPS_FORMAT
)

def create_dashboard():
    return Dashboard(
        title="Python generated example dashboard",
        description="Example dashboard using the Random Walk and default Prometheus datasource",
        tags=['example'],
        timezone="browser",
        panels=[
            TimeSeries(
                title="Random Walk",
                dataSource='default',
                targets=[Target(datasource='grafana', expr='example')],
                gridPos=GridPos(h=8, w=16, x=0, y=0),
            ),
            GaugePanel(
                title="Random Walk",
                dataSource='default',
                targets=[Target(datasource='grafana', expr='example')],
                gridPos=GridPos(h=4, w=4, x=17, y=0),
            ),
            TimeSeries(
                title="Prometheus http requests",
                dataSource='prometheus',
                targets=[
                    Target(
                        expr='rate(prometheus_http_requests_total[5m])',
                        legendFormat="{{ handler }}",
                        refId='A',
                    ),
                ],
                unit=OPS_FORMAT,
                gridPos=GridPos(h=8, w=16, x=0, y=10),
            ),
        ],
    ).auto_panel_ids()

def main():
    dashboard = create_dashboard()
    print("Dashboard object created successfully:")
    print(dashboard)

if __name__ == "__main__":
    main()
