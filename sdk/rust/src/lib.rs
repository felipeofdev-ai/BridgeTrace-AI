use reqwest::Client;
use serde_json::json;

pub struct BridgeTraceSdk {
    base_url: String,
    api_key: Option<String>,
    tenant_id: String,
    client: Client,
}

impl BridgeTraceSdk {
    pub fn new(base_url: &str, api_key: Option<String>, tenant_id: &str) -> Self {
        Self {
            base_url: base_url.trim_end_matches('/').to_string(),
            api_key,
            tenant_id: tenant_id.to_string(),
            client: Client::new(),
        }
    }

    pub async fn trace(&self, source_id: &str) -> Result<serde_json::Value, reqwest::Error> {
        let mut req = self.client
            .post(format!("{}/api/v2/trace", self.base_url))
            .header("X-Tenant-ID", &self.tenant_id)
            .json(&json!({"source_id": source_id, "max_hops": 5, "min_amount": 0}));

        if let Some(k) = &self.api_key {
            req = req.header("X-API-Key", k);
        }

        let res = req.send().await?;
        let json = res.json::<serde_json::Value>().await?;
        Ok(json)
    }
}
