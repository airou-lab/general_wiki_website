import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { Assets } from "./quartz/plugins/emitters/assets"
import { Static } from "./quartz/plugins/emitters/static"
import { ComponentResources } from "./quartz/plugins/emitters/componentResources"

const config = await loadQuartzConfig()

if (!config.plugins.emitters) {
    config.plugins.emitters = []
}
// Force inject missing emitters because YAML config doesn't load them properly
config.plugins.emitters.push(Assets())
config.plugins.emitters.push(Static())
config.plugins.emitters.push(ComponentResources())

export default config
export const layout = await loadQuartzLayout()
